function solve(array){
    let result = [];

    for(let i = 0; i < array.length; i++){
        let width = array[i][0];
        let height = array[i][1];
        let obj = {
            width,
            height,
            area: () => {
                return width * height;
            },
            compareTo: (other) =>{
                if((this.area() - other.area()) > 0){
                    return "larger";
                } else if((this.area() - other.area()) === 0){
                    return "equal";
                } else{
                    return "smaller";
                }
            }
        }

        result.push(obj);
    }

    result.sort((a,b) =>{
        if((a.area() - b.area()) !== 0){
            return b.area() - a.area();
        }
        
        return b.width - a.width;
    })

    console.log(result);
}

solve([[10,5], [3,20], [5,12]])