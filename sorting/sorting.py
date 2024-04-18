
class sorting:

    def bubble(self,input):
        for i in range(len(input)):

            for j in range(1,len(input)-i):
                if input[j-1] > input[j]:
                    tmp = input[j];
                    input[j] = input[j-1];
                    input[j-1] = tmp;


    def selection(self,input):
        for i in range(len(input)):
            k = i;
            for j in range(i,len(input)):
                if input[k] > input[j]:
                    k = j;
            tmp = input[i];
            input[i] = input[k];
            input[k] = tmp;



sort = sorting();
input = [2,10,8,7];
#sort.bubble(input);
print(input);
input = [10,5,8,20,2,18];
input = [3,1,5,2,10,8,4,7,6,9,0];
sort.selection(input);
#sort.bubble(input);
print(input);
