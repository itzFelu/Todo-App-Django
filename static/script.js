document.querySelector('.add-task-btn').addEventListener('click',(e)=>{
    console.log('add button pressed');
    window.location.href='/addtask'
})

document.querySelector('.task-list').addEventListener('click',(e)=>{
    console.log("inside tasklist");
    window.location.href='/tasklist';
})
document.querySelector('.todo').addEventListener('click',(e)=>{
    window.location.href='/';
})
function taskDetails(id){
    window.location.href=`taskDetails/${id}`
}
function delete_task(id) {
    if(confirm("are you sure you want to delete?")){
        console.log(`delete_task/${id}`);
        window.location.href=`delete_task/${id}`;
    }
}
function del_all(){
    console.log("clicked");
    let str="Type 'Delete All' to confirm"
    while(true){
        let res=prompt(str)
        if (res == 'Delete All'){
            console.log('correct');
            window.location.href='/deleteAll';
            break;
        }
        else if(res!='' && !res)
            break;
        else
            str="Type Correctly: 'Delete All' to confirm"
    }
}
