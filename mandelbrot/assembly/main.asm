; xmm0 > tmp  :  xmm7  > delta 
; xmm1 > tmp  :  xmm8  > offseta 
; xmm2 > zr   :  xmm12 > 2.0
; xmm3 > zr0  :  xmm14 > 4.0 
; xmm4 > zi   :  r8    > bool
; xmm5 > a    :  r9    > iterations  
; xmm6 > b    :  r10   > dim  

section .data
    offseta: dq -2.0
    offsetb: dq -1.5
    range: dq 3.0
    dim: dq 100
    iterations: dq 1000

    two: dq 2.0
    four: dq 4.0

    true: db "00"
    false: db "  "
    nl: db 0, 10
section .text
    global _start

_start:
    mov r9, [iterations]        ; r9 = iterations
    movsd xmm5, [offseta]       ; xmm8 = offseta
    movsd xmm6, [offsetb]       ; xmm6 = offsetb
    movsd xmm8, xmm5            ; xmm8 = xmm5
    movsd xmm12, [two]          ; xmm12 = 2.0
    movsd xmm14, [four]         ; xmm14 = 4.0
    mov r10, [dim]              ; r10 = dim
    mov rcx, r10                ; rcx = dim

    movsd xmm0, [range]         ; xmm0 = range
    cvtsi2sd xmm1, r10          ; xmm1 = dim
    vdivsd xmm7, xmm0, xmm1     ; set delta to range/dim
    
y:
    push rcx                    ; push y loop counter
    mov rcx, r10                ; set x loop counter to dim

    x:
        push rcx                ; push x loop counter
        movsd xmm2, xmm5        ; set zr to a
        movsd xmm3, xmm5        ; set zr0 to a
        movsd xmm4, xmm6        ; set zi to b
        mov rcx, r9             ; set calc iteration counter to iterations
        call calc               ; call calc to begin iterating
        call print              ; print string
        addsd xmm5, xmm7        ; add delta to zr
        pop rcx                 ; pop x loop counter
        loop x                  ; loop x if x loop counter is not 0

    movsd xmm5, xmm8            ; reset a to offset
    addsd xmm6, xmm7            ; add delta to b
    mov rsi, nl                 ; set string to print to newline
    call print                  ; print string
    pop rcx                     ; pop y loop counter
    loop y                      ; loop y if y loop counter is not 0
jmp end                         ; jump to end of program

calc:
    push rcx
    mulsd xmm2, xmm2            ; zr^2
    vmulsd xmm0, xmm4, xmm4     ; zi^2
    subsd xmm2, xmm0            ; zr^2 - zi^2
    addsd xmm2, xmm5            ; zr^2 - zi^2 + a

    mulsd xmm4, xmm12           ; 2*zi
    mulsd xmm4, xmm3            ; 2*zi*zr
    addsd xmm4, xmm6            ; 2*zi*zr + b

    vmulsd xmm0, xmm2, xmm2     ; xmm0 = zr^2
    vmulsd xmm1, xmm4, xmm4     ; xmm1 = zi^2
    addsd xmm0, xmm1            ; xmm0 = zr^2 + zi^2
    cmpltsd xmm0, xmm14         ; xmm0 < 4.
    
    movq r8, xmm0               ; mov bool ans in xmm0 to r8
    test r8, r8                 ; test if bool ans is true
    jnz continue                ; if true continue
    mov rsi, true               ; else set string to print to true
    pop rax                     ; pop loop counter
    ret                         ; return
    
continue:
    movsd xmm3, xmm2            ; zr0 = zr
    pop rcx                     ; pop loop counter
    loop calc                   ; if rcx > 0 continue to iterate
    mov rsi, false              ; set string to print to false
    ret                         ; return

print:
    mov rax, 1                  ; set opcode to sys_write
    mov rdi, 1                  ; set file descriptor to stdout
    mov rdx, 2                  ; set string length to 2 bytes
    syscall                     ; call sys_write
    ret                         ; return

end:
    mov rax, 60                 ; set opcode to sys_exit
    mov rdi, 0                  ; set exit code to 0
    syscall                     ; call sys_exit