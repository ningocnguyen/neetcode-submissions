class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        # ensure A is the shorter array
        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2  # partition index for A
            j = half - i - 2  # partition index for B

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd: median is the minimum of the right elements
                if total % 2:
                    return float(min(Aright, Bright))
                # even: median is the average of middle boundaries
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1