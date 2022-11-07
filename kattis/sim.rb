gets.to_i.times{i=0
s=""
gets.chomp.split("").each{|x|
case x
when"]"
i=s.length
when"["
i=0
when"<"
if i>0
s[i-=1]=""end
else
s.insert i,x
i+=1
end}
puts s}