# @param {Integer[][]} intervals
# @return {Integer[][]}
def merge(intervals)
    return [] if intervals.empty?
    intervals = intervals.sort_by { |x| x[0] }
    result = [intervals[0]]
  
    intervals[1..-1].each do |i|
    if result[-1][1] >= i[0] 
      result[-1][1] = [result[-1][1], i[1]].max
    else
      result << i
    end
  end
  result
end