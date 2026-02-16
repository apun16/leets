# @param {Integer[][]} intervals
# @return {Integer[][]}
def merge(intervals)
    return [] if intervals.empty?
    intervals.sort! { |a, b| a[0] <=> b[0] }
    result = [intervals[0]]
    current = result[0]
      
    intervals[1..].each do |next_interval|
    if current[1] >= next_interval[0]
      current[1] = [current[1], next_interval[1]].max
    else
      current = next_interval
      result << current
    end
  end
  result
end