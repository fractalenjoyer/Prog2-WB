gets.to_i.times{
a=[[],[]]
i=a[1]
gets.chomp.chars.each{|x|
if'['==x
a[0].push[]
i=a[0][-1]
elsif']'==x
i=a[1]
elsif'<'==x
i.pop
else
i.push x
end
}
a[0].reverse!
puts a.join
}