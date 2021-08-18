
#  it have timecomplexity of O(n+m)
def nedianoftwosortedArray(nums1,nums2):
    i=j=0
    r = []
    l1,l2,l3= len(nums1),len(nums2),len(nums1)+len(nums2)
    if l1==0 and l2 == 0:
        return 0
    elif l1==0:
        return nums2[l2//2]/1 if l2%2==1 else (nums2[(l2//2)-1]+nums2[(l2//2)])/2
    elif l2==0:
        return nums1[l1//2]/1 if l1%2==1 else (nums1[(l1//2)-1]+nums1[(l1//2)])/2
    
    for k in range(l1+l2):
        if i < l1 and j < l2:
            if nums1[i] < nums2[j]:
                r.append(nums1[i])
                i+=1
            else:
                r.append(nums2[j])
                j+=1
    while i < l1:
        r.append(nums1[i])
        i+=1
    while j < l2:
        r.append(nums2[j])
        j+=1
    print(r)
    return r[(l3//2)]//1 if l3%2==1 else (r[(l3//2)-1]+r[(l3//2)])/2

#  it have time complexity of O(nlog(m))

def nedianoftwosortedArray1(nums1,nums2):
    i=j=0
    r = []
    l1,l2,l3= len(nums1),len(nums2),len(nums1)+len(nums2)
    if l1==0 and l2 == 0:
        return 0
    elif l1==0:
        return nums2[l2//2]/1 if l2%2==1 else (nums2[(l2//2)-1]+nums2[(l2//2)])/2
    elif l2==0:
        return nums1[l1//2]/1 if l1%2==1 else (nums1[(l1//2)-1]+nums1[(l1//2)])/2
    else:
        
        nums1 = nums1.extend(nums2)
        
        r = sorted(nums1)
        print(r)
        return r[(l3//2)]//1 if l3%2==1 else (r[(l3//2)-1]+r[(l3//2)])/2

nums1,nums2 = [1,2],[3]
nedianoftwosortedArray1(nums1,nums2)
