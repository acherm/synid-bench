//
//  TreeViewController.m
//  MYT
//
//  Created by yunruiinfo on 16/1/15.
//  Copyright © 2016年 YunRui. All rights reserved.
//

#import "TreeViewController.h"
#import "Node.h"
#import "ButtomView.h"
#import "ProductdetalViewController.h"
#import"Utility.h"
#import "MJRefresh.h"
@interface TreeViewController ()
{
    NSString *parent;
    NSString *pparent;
    NSString *child;
    NSArray *init;
    NSString* mat;//物料id
    NSMutableArray *nodear;//所有node数据
    NSMutableArray *_tempedata;//要显示的所有数据
    __block  NSMutableArray  *typearr;//存类型为T的物料类别
    __block  NSMutableArray  *wularr;//存类型为W的物料类别
    NSMutableArray *typea;
    NSMutableArray *wula;
    NSMutableArray *ndone;
    BOOL findclick;
    int zf;
    BOOL iffindtext;
}
@end

@implementation TreeViewController
-(void)viewWillAppear:(BOOL)animated
{
    findclick=NO;
    ButtomView* BtmV=[[ButtomView alloc]initWithFrame:CGRectMake(0, ScreenHeight-49, ScreenWidth, 50)];
    [self.view addSubview:BtmV];
     self.navigationController.navigationBarHidden=NO;
   
    
}
-(void)initwithnodear
{
    [_tempedata removeAllObjects];
    for (int i=0; i<nodear.count; i++) {
        for (int j=0; j<((NSMutableArray*)[nodear objectAtIndex:i]).count; j++) {
            [_tempedata addObject:[(NSMutableArray*)[nodear objectAtIndex:i] objectAtIndex:j]];
        }
    }//暂时测试2级
   // [_tableView reloadData];
}

- (void)viewDidLoad {
    iffindtext=NO;
    _tableView.delegate=self;
    _tableView.dataSource=self;
    _tempedata=[[NSMutableArray alloc]init];
    nodear=[[NSMutableArray alloc] init];
    typearr=[[NSMutableArray alloc]init];
    wularr=[[NSMutableArray alloc]init];
    
    ndone=[[NSMutableArray alloc]init];
    typea=[[NSMutableArray alloc]init];
    wula=[[NSMutableArray alloc]init];
    
    _tableView.mj_footer = [MJRefreshBackNormalFooter footerWithRefreshingTarget:self refreshingAction:@selector(loadMoreData)];
    _findtext.delegate=self;
    _findview.hidden=YES;
    zf=1;
    for(int i=0;i<_nodearr.count;i++)
    {
        NSMutableArray *nodea=[[NSMutableArray alloc]init];//创建每行
        [nodea addObject:[_nodearr objectAtIndex:i]];//将第一层的node分别加入不同的可变数组
        
        [nodear addObject:nodea];
    }
    //消除多余空白行
    UIView *view = [UIView new];
    view.backgroundColor = [UIColor clearColor];
    [self.tableView setTableFooterView:view];
    
    [self initwithnodear];
    NSLog(@"%@",_tempedata);
   // UISwipeGestureRecognizer* recognizer;
    // handleSwipeFrom 是偵測到手势，所要呼叫的方法
   // recognizer = [[UITapGestureRecognizer alloc] initWithTarget:self action:@selector(closefind)];
    // 不同的 Recognizer 有不同的实体变数
    // 例如 SwipeGesture 可以指定方向
    // 而 TapGesture 則可以指定次數
  //  [self.view addGestureRecognizer:recognizer];
    //设置搜索框的代理
    _stocksearch.delegate=self;
    [super viewDidLoad];
    // Do any additional setup after loading the view.
}

//////第一级搜索
- (void)searchBar:(UISearchBar *)searchBar textDidChange:(NSString *)searchText
{
   
    zf=1;
    NSString *find=[searchText stringByReplacingPercentEscapesUsingEncoding:NSUTF8StringEncoding];
    NSString *findtext = [find stringByReplacingOccurrencesOfString:@" " withString:@""];
    if ([findtext  isEqualToString:@""]) {
        iffindtext=NO;
    }
    else
        iffindtext=YES;
    [nodear removeAllObjects];
    [ndone removeAllObjects];
    [typea removeAllObjects];
    [wula removeAllObjects];
    NSLog(@"%@",ndone);
    NSString *pagenum=[NSString stringWithFormat:@"%d",zf];
    NSMutableDictionary* parDic=[[NSMutableDictionary alloc]initWithCapacity:10];
    [parDic setValue:[[NSUserDefaults standardUserDefaults]objectForKey:@"user_id"] forKey:@"userid"];
    NSLog(@"%@",[[NSUserDefaults standardUserDefaults]objectForKey:@"user_id"]);
    [parDic setValue:@"null" forKey:@"parentid"];
    [parDic setValue:pagenum forKey:@"pageNum"];
    if (iffindtext) {
        [parDic setValue:findtext forKey:@"search"];
    }
    [parDic setValue:@"5" forKey:@"pageSize"];//依次请求
    dispatch_queue_t concurrentQueue = dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0);
    
    dispatch_sync(concurrentQueue, ^{
        [[QQRequestManager sharedRequestManager] GET:[SEVER_URL stringByAppendingString:@"yd/getMatTree.action"] parameters:parDic showHUD:YES success:^(NSURLSessionDataTask *task, id responseObject) {
            
            _totlePage=((NSNumber*)[responseObject objectForKey:@"totlePage"]).intValue;
            init=[responseObject objectForKey:@"list"];
            for (NSDictionary *dic in init) {
                if ([[dic objectForKey:@"tw"] isEqualToString:@"T"]) {
                    [typea addObject:dic];
                }
                else
                {
                    [wula addObject:dic];
                }
            }
            for (int i=0; i<typea.count; i++) {
                NSDictionary * typeinfo=[typea objectAtIndex:i];
                NSString* nodeid=[typeinfo objectForKey:@"typeid"];
                int counts=((NSNumber*)[typeinfo objectForKey:@"counts"]).intValue;
                int matecounts=((NSNumber*)[typeinfo objectForKey:@"matecounts"]).intValue;
                Node * node=[[Node alloc]initWithParentId:@"-1" nodeId:nodeid name:[typeinfo objectForKey:@"typename"] depth:0 expand:YES child:YES matid:@"-1" counts:counts matecounts:matecounts];
                [ndone addObject:node];
            }
            for (int i=0; i<wula.count; i++) {
                NSDictionary * wulinfo=[wula objectAtIndex:i];
                NSString* nodeid=[wulinfo objectForKey:@"matid"];
                int counts=((NSNumber*)[wulinfo objectForKey:@"counts"]).intValue;
                int matecounts=((NSNumber*)[wulinfo objectForKey:@"matecounts"]).intValue;
                Node * node=[[Node alloc]initWithParentId:@"-1" nodeId:nodeid name:[wulinfo objectForKey:@"mattername"] depth:0 expand:YES child:NO matid:@"-1" counts:counts matecounts:matecounts];
                [ndone addObject:node];
                
            }
            NSLog(@"%@",ndone);
            
            for(int i=0;i<ndone.count;i++)
            {
                NSMutableArray *nodea=[[NSMutableArray alloc]init];//创建每行
                [nodea addObject:[_nodearr objectAtIndex:i]];//将第一层的node分别加入不同的可变数组
                
                [nodear addObject:nodea];
            }
            
            [self initwithnodear];
          
                [_tableView reloadData];
            

            
            //将请求到的第一层数据分类
        } failure:^(NSURLSessionDataTask *task, NSError *error) {
            
            
            [self qq_performSVHUDBlock:^{
                [SVProgressHUD showErrorWithStatus:@"请求数据失败"];
            }];
        }];
        
        /*download the image here*/
        
    });
}

//////加载更多////////
- (void)loadMoreData
{
    NSString *find=[_stocksearch.text stringByReplacingPercentEscapesUsingEncoding:NSUTF8StringEncoding];
    NSString *findtext = [find stringByReplacingOccurrencesOfString:@" " withString:@""];
    // 1.添加假数据
    if (zf<_totlePage+1) {
        zf++;
        [ndone removeAllObjects];
        [typea removeAllObjects];
        [wula removeAllObjects];
        NSLog(@"%@",ndone);
        NSString *pagenum=[NSString stringWithFormat:@"%d",zf];
        NSMutableDictionary* parDic=[[NSMutableDictionary alloc]initWithCapacity:10];
        [parDic setValue:[[NSUserDefaults standardUserDefaults]objectForKey:@"user_id"] forKey:@"userid"];
        NSLog(@"%@",[[NSUserDefaults standardUserDefaults]objectForKey:@"user_id"]);
        if (iffindtext) {
            [parDic setValue:findtext forKey:@"search"];
        }
        [parDic setValue:@"null" forKey:@"parentid"];
        [parDic setValue:pagenum forKey:@"pageNum"];
        [parDic setValue:@"5" forKey:@"pageSize"];//依次请求
        dispatch_queue_t concurrentQueue = dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0);
        
        dispatch_sync(concurrentQueue, ^{
            [[QQRequestManager sharedRequestManager] GET:[SEVER_URL stringByAppendingString:@"yd/getMatTree.action"] parameters:parDic showHUD:YES success:^(NSURLSessionDataTask *task, id responseObject) {
                
               
                init=[responseObject objectForKey:@"list"];
                for (NSDictionary *dic in init) {
                    if ([[dic objectForKey:@"tw"] isEqualToString:@"T"]) {
                        [typea addObject:dic];
                    }
                    else
                    {
                        [wula addObject:dic];
                    }
                }
                for (int i=0; i<typea.count; i++) {
                    NSDictionary * typeinfo=[typea objectAtIndex:i];
                    NSString* nodeid=[typeinfo objectForKey:@"typeid"];
                    int counts=((NSNumber*)[typeinfo objectForKey:@"counts"]).intValue;
                    int matecounts=((NSNumber*)[typeinfo objectForKey:@"matecounts"]).intValue;
                    Node * node=[[Node alloc]initWithParentId:@"-1" nodeId:nodeid name:[typeinfo objectForKey:@"typename"] depth:0 expand:YES child:YES matid:@"-1" counts:counts matecounts:matecounts];
                    [ndone addObject:node];
                }
                for (int i=0; i<wula.count; i++) {
                    NSDictionary * wulinfo=[wula objectAtIndex:i];
                    NSString* nodeid=[wulinfo objectForKey:@"matid"];
                    int counts=((NSNumber*)[wulinfo objectForKey:@"counts"]).intValue;
                    int matecounts=((NSNumber*)[wulinfo objectForKey:@"matecounts"]).intValue;
                    Node * node=[[Node alloc]initWithParentId:@"-1" nodeId:nodeid name:[wulinfo objectForKey:@"mattername"] depth:0 expand:YES child:NO matid:@"-1" counts:counts matecounts:matecounts];
                    [ndone addObject:node];
                    
                }
                NSLog(@"%@",ndone);
                for(int i=0;i<ndone.count;i++)
                {
                    NSMutableArray *nodea=[[NSMutableArray alloc]init];//创建每行
                    [nodea addObject:[ndone objectAtIndex:i]];//将第一层的node分别加入不同的可变数组
                    
                    [nodear addObject:nodea];
                }
                [self initwithnodear];
                [_tableView reloadData];
                //将请求到的第一层数据分类
            } failure:^(NSURLSessionDataTask *task, NSError *error) {
                
                
                [self qq_performSVHUDBlock:^{
                    [SVProgressHUD showErrorWithStatus:@"请求数据失败"];
                }];
            }];
            
            /*download the image here*/
            
        });
        zf++;
    }
    else
    {
        [SVProgressHUD showErrorWithStatus:@"已经到底啦"];
    }
    
    
    
    // 2.模拟2秒后刷新表格UI（真实开发中，可以移除这段gcd代码）
    
    // 刷新表格
    
    
    // 拿到当前的上拉刷新控件，结束刷新状态
    [_tableView.mj_footer endRefreshing];
    
}
-(NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section{
    NSLog(@"%d",_tempedata.count);
    return _tempedata.count;
}
- (NSInteger)numberOfSectionsInTableView:(UITableView *)tableView
{
    return 1;
}

// Row display. Implementers should *always* try to reuse cells by setting each cell's reuseIdentifier and querying for available reusable cells with dequeueReusableCellWithIdentifier:
// Cell gets various attributes set automatically based on table (separators) and data source (accessory views, editing controls)

- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
    Node *node = [_tempedata objectAtIndex:indexPath.row];
    
    static NSString *NODE_CELL_ID ;
    if (node.depth==0||node.depth==1) {
        NODE_CELL_ID = @"node_cell_id0";
        
        
        
    }
    /*else if(node.depth==1)
     {
     NODE_CELL_ID = @"node_cell_id1";
     }*/
    else if(node.depth==2)
    {
        NODE_CELL_ID = @"node_cell_id2";
    }
    UITableViewCell *cell=[tableView dequeueReusableCellWithIdentifier:NODE_CELL_ID];
    if (!cell) {
            if (node.depth==0||node.depth==1) {
        cell = [[UITableViewCell alloc] initWithStyle:UITableViewCellStyleDefault reuseIdentifier:NODE_CELL_ID];
            //数量
            UILabel* count;
            count=[[UILabel alloc]initWithFrame:CGRectMake(ScreenWidth/2-40, 15, 80, 15)];
        
            count.tag=11;
            count.textColor=[UIColor redColor];
            count.font=[UIFont systemFontOfSize:14];
            count.textAlignment=NSTextAlignmentCenter;
            [cell.contentView addSubview:count];
            
            //匹配客户
            UILabel* men;
            men=[[UILabel alloc]initWithFrame:CGRectMake(ScreenWidth-80, 15, 80, 15)];
            men.tag=12;
            men.textColor=[UIColor greenColor];
            men.font=[UIFont systemFontOfSize:14];
            men.textAlignment=NSTextAlignmentCenter;
            [cell.contentView addSubview:men];
            
            UIImageView *image=[[UIImageView alloc] init];
            image.tag=13;
            //if(node.child)
            // {
            
           
        
            
            
            //image.image=[UIImage imageNamed:@"left"];
            [cell.contentView addSubview:image];
        }
            else if (node.depth==2)
            {
                cell = [[UITableViewCell alloc] initWithStyle:UITableViewCellStyleDefault reuseIdentifier:NODE_CELL_ID];
                UILabel* count;
                count=[[UILabel alloc]initWithFrame:CGRectMake(ScreenWidth/2-40, 15, 80, 15)];
                
                count.tag=11;
                count.textColor=[UIColor redColor];
                count.font=[UIFont systemFontOfSize:14];
                count.textAlignment=NSTextAlignmentCenter;
                [cell.contentView addSubview:count];
                
                //匹配客户
                UILabel* men;
                men=[[UILabel alloc]initWithFrame:CGRectMake(ScreenWidth-80, 15, 80, 15)];
                men.tag=12;
                men.textColor=[UIColor greenColor];
                men.font=[UIFont systemFontOfSize:14];
                men.textAlignment=NSTextAlignmentCenter;
                [cell.contentView addSubview:men];

              //  UITextField *text = [[UITextField alloc]initWithFrame:CGRectMake(20, 0, 130, 30)];
              //  text.borderStyle = UITextBorderStyleRoundedRect;
              //  text.text=@"1";
               // [cell.contentView addSubview:text];
                //设置边框样式，只有设置了才会显示边框样式
                
              //  text.borderStyle = UITextBorderStyleRoundedRect;
            }

    }
    UILabel* label2=(UILabel*)[cell.contentView viewWithTag:11];
    label2.font=[UIFont systemFontOfSize:14];
    label2.text=[NSString stringWithFormat:@"%d",node.counts];
    
    UILabel* label3=(UILabel*)[cell.contentView viewWithTag:12];
    label2.font=[UIFont systemFontOfSize:14];
    label3.text=[NSString stringWithFormat:@"%d",node.matecounts];
    
    UIImageView *image=(UIImageView*)[cell.contentView viewWithTag:13];
    if (node.depth==0) {
        NSLog(@"%@",node.name);
        image.frame=CGRectMake(2, 16,8, 8);
    }
    
    else if(node.depth==1)
    {
        NSLog(@"%@",node.name);
        image.frame=CGRectMake(25, 16,8, 8);
        //image.frame=CGRectMake(2, 16,8, 8);
    }
    image.image=[UIImage imageNamed:@"公司库存向右"];
    
    
    
    //
    // cell有缩进的方法
    cell.indentationLevel = node.depth; // 缩进级别
    cell.indentationWidth = 20.f; // 每个缩进级别的距离
    
    
    //    NSMutableString *name = [NSMutableString string];
    //    for (int i=0; i<node.depth; i++) {
    //        [name appendString:@"     "];
    //    }
    
    //    [name appendString:node.name];
    cell.textLabel.font=[UIFont systemFontOfSize:14];
    cell.textLabel.text = node.name;

    return cell;
}


- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}
- (void)tableView:(UITableView *)tableView didSelectRowAtIndexPath:(NSIndexPath *)indexPath{
    init=[[NSArray alloc]init];
    UITableViewCell *cell = [self.tableView cellForRowAtIndexPath:indexPath];
     Node *parentNode = [_tempedata objectAtIndex:indexPath.row];
 NSLog(@"%hd",parentNode.child);
    NSLog(@"%hd",parentNode.expand);
    NSLog(@"%@",nodear);
    if(![parentNode.matid isEqual:@"-1"])
    {
        for(Node *nd in _tempedata)
        {
        if (nd.nodeId==parentNode.parentId) {
            parent=nd.name;
            for (Node *ndd in _tempedata) {
                if (ndd.nodeId==nd.parentId) {
                    pparent=ndd.name;
                    child=parentNode.name;
                    mat=parentNode.matid;
                }
            }
        }
        }
        [self performSegueWithIdentifier:@"product" sender:self];
    }
    __block  NSUInteger startPosition = indexPath.row+1;
    __block  NSUInteger endPosition = startPosition;
    
    if(parentNode.depth==0&&parentNode.child)
    {
        NSMutableArray * arr=[[NSMutableArray alloc]init];
        __block int j;
        for (int i=0;i<_nodearr.count;i++) {
            if (((Node*)[_nodearr objectAtIndex:i]).nodeId==parentNode.nodeId) {
                arr=(NSMutableArray*)[nodear objectAtIndex:i];
                j=i;
            }
        }
        
        NSMutableDictionary* parDic=[[NSMutableDictionary alloc]initWithCapacity:10];
        [parDic setValue:[[NSUserDefaults standardUserDefaults]objectForKey:@"user_id"] forKey:@"userid"];
        NSLog(@"%@",[[NSUserDefaults standardUserDefaults]objectForKey:@"user_id"]);
        NSString *nodeid=[NSString stringWithFormat:@"%@",parentNode.nodeId];
        [parDic setValue:nodeid forKey:@"parentid"];
        [parDic setValue:@"1" forKey:@"pageNum"];
        [parDic setValue:@"10000" forKey:@"pageSize"];
        [[QQRequestManager sharedRequestManager] GET:[SEVER_URL stringByAppendingString:@"yd/getMatTree.action"] parameters:parDic showHUD:YES success:^(NSURLSessionDataTask *task, id responseObject) {
            NSLog(@"%@",responseObject);
            init=[responseObject objectForKey:@"list"];
            for (NSDictionary *dic in init) {
                if ([[dic objectForKey:@"tw"] isEqualToString:@"T"]) {
                    [typearr addObject:dic];
                }
                else
                {
                    [wularr addObject:dic];
                }
            }
            for (int i=0; i<typearr.count; i++) {
                NSDictionary * typeinfo=[typearr objectAtIndex:i];
                NSString* nodeid=[typeinfo objectForKey:@"typeid"];
                int counts=((NSNumber*)[typeinfo objectForKey:@"counts"]).intValue;
                int matecounts=((NSNumber*)[typeinfo objectForKey:@"matecounts"]).intValue;
                Node * node1=[[Node alloc]initWithParentId:parentNode.nodeId nodeId:nodeid name:[typeinfo objectForKey:@"typename"] depth:1 expand:YES child:YES matid:@"-1" counts:counts matecounts:matecounts];
                
                if (parentNode.expand) {
                    NSLog(@"%@",[nodear objectAtIndex:j]);
                    [(NSMutableArray*)[nodear objectAtIndex:j] addObject:node1];//增加
                    endPosition++;
                  
                    
                }
                
            }
            
            for (int i=0; i<wularr.count; i++) {
                NSDictionary * wulinfo=[wularr objectAtIndex:i];
                NSString* nodeid=[wulinfo objectForKey:@"matid"];
                int counts=((NSNumber*)[wulinfo objectForKey:@"counts"]).intValue;
                int matecounts=((NSNumber*)[wulinfo objectForKey:@"matecounts"]).intValue;
                Node * node1=[[Node alloc]initWithParentId:parentNode.nodeId nodeId:nodeid name:[wulinfo objectForKey:@"mattername"] depth:1 expand:NO child:NO matid:nodeid counts:counts matecounts:matecounts];
                if(parentNode.expand)
                {
                [(NSMutableArray*)[nodear objectAtIndex:j] addObject:node1];
                    endPosition++;
                }
            }
            if (!parentNode.expand) {
                NSLog(@"%@",(NSMutableArray*)[nodear objectAtIndex:j]);
                NSLog(@"%lu",(unsigned long)((NSMutableArray*)[nodear objectAtIndex:j]).count);
                int numj=((NSMutableArray*)[nodear objectAtIndex:j]).count;
                for (int i=1; i<numj; i++) {
                    Node * nod=[(NSMutableArray*)[nodear objectAtIndex:j] objectAtIndex:1];
                    
                    [(NSMutableArray*)[nodear objectAtIndex:j] removeObject:nod];//移除
                    NSLog(@"%@",(NSMutableArray*)[nodear objectAtIndex:j]);
                }
            }
           
            if (!parentNode.expand) {
                endPosition = [self removeAllNodesAtParentNode:parentNode];
            }
           
            NSLog(@"%@",nodear);
            [typearr removeAllObjects];
            [wularr removeAllObjects];
            [self initwithnodear];
           
            NSMutableArray *indexPathArray = [NSMutableArray array];
            //修正indexpath
            for (NSUInteger i=startPosition; i<endPosition; i++) {
                NSIndexPath *tempIndexPath = [NSIndexPath indexPathForRow:i inSection:0];
                [indexPathArray addObject:tempIndexPath];
            }
            if (parentNode.expand) {
                [self.tableView insertRowsAtIndexPaths:indexPathArray withRowAnimation:UITableViewRowAnimationNone];
            }else{
                [self.tableView deleteRowsAtIndexPaths:indexPathArray withRowAnimation:UITableViewRowAnimationNone];
            }
        
              parentNode.expand=!parentNode.expand;
        } failure:^(NSURLSessionDataTask *task, NSError *error) {
            
            
            [self qq_performSVHUDBlock:^{
                [SVProgressHUD showErrorWithStatus:@"账号或密码错误"];
            }];
        }];
        
        //  }
        // else
        // {
        
        // }
        
    }//第2级可能有物料规格可能有物料
    else if (parentNode.depth==1&&parentNode.child)
    {
        NSMutableArray * arr=[[NSMutableArray alloc]init];
        NSMutableArray* insertdic=[[NSMutableArray alloc]init];
        
        __block int j;
        __block int k;
        for (int i=0;i<nodear.count;i++) {
            
            for (int z=0; z<((NSMutableArray*)[nodear objectAtIndex:i]).count; z++) {
                arr=(NSMutableArray*)[nodear objectAtIndex:i];//获取第2层全部
                NSLog(@"%@he%@",((Node*)[arr objectAtIndex:z]).nodeId,parentNode.nodeId);
                if ([((Node*)[arr objectAtIndex:z]).nodeId isEqual:parentNode.nodeId]) {
                    j=z;//获得第2层的插入位置
                    k=i;//获取在nodear中相对于哪一个数组
                    break;
                }
            }
           // if (((Node*)[_nodearr objectAtIndex:i]).nodeId==parentNode.nodeId) {
             //   arr=(NSMutableArray*)[nodear objectAtIndex:i];
               // j=i;
            //}
        }
        
        NSLog(@"%@",nodear);
        NSMutableDictionary* parDic=[[NSMutableDictionary alloc]initWithCapacity:10];
        [parDic setValue:[[NSUserDefaults standardUserDefaults]objectForKey:@"user_id"] forKey:@"userid"];
        NSLog(@"%@",[[NSUserDefaults standardUserDefaults]objectForKey:@"user_id"]);
        NSString *nodeid=[NSString stringWithFormat:@"%@",parentNode.nodeId];
        [parDic setValue:nodeid forKey:@"parentid"];
        [parDic setValue:@"1" forKey:@"pageNum"];
        [parDic setValue:@"10000" forKey:@"pageSize"];
        [[QQRequestManager sharedRequestManager] GET:[SEVER_URL stringByAppendingString:@"yd/getMatTree.action"] parameters:parDic showHUD:YES success:^(NSURLSessionDataTask *task, id responseObject) {
            NSLog(@"%@",responseObject);
            init=[responseObject objectForKey:@"list"];
            for (NSDictionary *dic in init) {
                if ([[dic objectForKey:@"tw"] isEqualToString:@"T"]) {
                    [typearr addObject:dic];
                }
                else
                {
                    [wularr addObject:dic];
                }
            }//第3级默认全部是物料了
          NSLog(@"%hd",parentNode.expand);
                for (int i=0; i<wularr.count; i++) {
                NSDictionary * wulinfo=[wularr objectAtIndex:i];
                    NSString* nodeid=[wulinfo objectForKey:@"matid"];
                int counts=((NSNumber*)[wulinfo objectForKey:@"counts"]).intValue;
                int matecounts=((NSNumber*)[wulinfo objectForKey:@"matecounts"]).intValue;
                    Node * node1=[[Node alloc]initWithParentId:parentNode.nodeId nodeId:nodeid name:[wulinfo objectForKey:@"mattername"] depth:2 expand:NO child:NO matid:nodeid counts:counts matecounts:matecounts];
               NSLog(@"%hd",parentNode.expand);
                    if (parentNode.expand) {
                      //  NSLog(@"%@",[nodear objectAtIndex:j]);
                       [(NSMutableArray*)[nodear objectAtIndex:k] insertObject:node1 atIndex:j+i+1];//增加
                        endPosition++;
                        
                        
                    }
                    else
                    {
                        NSLog(@"%@",nodear);
                        for (int i=indexPath.row+1; i<((NSMutableArray*)[nodear objectAtIndex:k]).count; i++) {
                            Node * nod=[(NSMutableArray*)[nodear objectAtIndex:k] objectAtIndex:indexPath.row+1];
                            if ([nod.nodeId isEqualToString:nodeid]) {
                                [(NSMutableArray*)[nodear objectAtIndex:k] removeObject:nod];//移除
                            }
                            NSLog(@"%@",nodear);
                            
                        }
                        
                        
                    }

                
            }
            if (!parentNode.expand) {
                endPosition = [self removeAllNodesAtParentNode:parentNode];
            }
            
            NSLog(@"%@",nodear);
            
            NSLog(@"%@",nodear);
            [typearr removeAllObjects];
            [wularr removeAllObjects];
            [self initwithnodear];
            
            NSMutableArray *indexPathArray = [NSMutableArray array];
            //修正indexpath
            for (NSUInteger i=startPosition; i<endPosition; i++) {
                NSIndexPath *tempIndexPath = [NSIndexPath indexPathForRow:i inSection:0];
                [indexPathArray addObject:tempIndexPath];
            }
            if (parentNode.expand) {
                [self.tableView insertRowsAtIndexPaths:indexPathArray withRowAnimation:UITableViewRowAnimationNone];
            }else{
                [self.tableView deleteRowsAtIndexPaths:indexPathArray withRowAnimation:UITableViewRowAnimationNone];
            }
            
            parentNode.expand=!parentNode.expand;
        } failure:^(NSURLSessionDataTask *task, NSError *error) {
            
            
            [self qq_performSVHUDBlock:^{
                [SVProgressHUD showErrorWithStatus:@"账号或密码错误"];
            }];
        }];
    }
    
    if(parentNode.expand)
    {
        UIImageView *image=(UIImageView*)[cell.contentView viewWithTag:13];
        image.image=[UIImage imageNamed:@"公司库存向下"];
    }
    else
    {
        UIImageView *image=(UIImageView*)[cell.contentView viewWithTag:13];
        image.image=[UIImage imageNamed:@"公司库存向右"];
    }
}
/**
 *  删除该父节点下的所有子节点（包括孙子节点）
 *
 *  @param parentNode 父节点
 *
 *  @return 该父节点下一个相邻的统一级别的节点的位置
 */
-(NSUInteger)removeAllNodesAtParentNode : (Node *)parentNode{
   
    NSUInteger startPosition = [_tempedata indexOfObject:parentNode];
    NSLog(@"%d",parentNode.depth);
    NSLog(@"%d",startPosition);
    NSUInteger endPosition = startPosition;
    for (NSUInteger i=startPosition+1; i<_tempedata.count; i++) {
        Node *node = [_tempedata objectAtIndex:i];
        endPosition++;
        if (node.depth <= parentNode.depth) {
            break;
        }
        if(endPosition == _tempedata.count-1){
            endPosition++;
            node.expand = NO;
            break;
        }
        node.expand = NO;
    }
    if (endPosition>startPosition) {
        [_tempedata removeObjectsInRange:NSMakeRange(startPosition+1, endPosition-startPosition-1)];
    }
    return endPosition;
}
- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender
{
    if ([segue.identifier isEqual:@"product"]) {
        ProductdetalViewController *product=segue.destinationViewController;
        product.depth0=pparent;
        product.depth1=parent;
        product.depth2=child;
        product.matid=mat;
    }
}
/*
#pragma mark - Navigation

// In a storyboard-based application, you will often want to do a little preparation before navigation
- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender {
    // Get the new view controller using [segue destinationViewController].
    // Pass the selected object to the new view controller.
}
*/
-(NSIndexPath *)tableView:(UITableView *)tableView
 willSelectRowAtIndexPath:(NSIndexPath *)indexPath
{
    [_stocksearch resignFirstResponder];
     [_findtext resignFirstResponder];
    return indexPath;
}
- (IBAction)click_find:(id)sender {
    NSString *findtext = [_findtext.text stringByReplacingOccurrencesOfString:@" " withString:@""];
    if ([findtext isEqualToString:@""]) {
        [self qq_performSVHUDBlock:^{
            [SVProgressHUD showErrorWithStatus:@"请输入搜索内容"];
        }];
    }//空的话
    else
    {
        NSLog(@"%@",findtext);
        NSLog(@"%@",_tempedata);
        for (int i=0;i<_tempedata.count;i++) {
            Node *node=(Node*)[_tempedata objectAtIndex:i];
            NSLog(@"%@",node.name);
            if ([node.name rangeOfString:findtext].location !=NSNotFound) {
                NSLog(@"找到了");
                NSUInteger sectionCount = [self.tableView numberOfSections];
                if (sectionCount) {
                    NSUInteger rowCount = i;
                    if (rowCount) {
                        NSUInteger ii[2] = {0, i};
                        NSIndexPath* indexPath = [NSIndexPath indexPathWithIndexes:ii length:2];
                        [self.tableView scrollToRowAtIndexPath:indexPath
                                              atScrollPosition:UITableViewScrollPositionBottom animated:YES];  
                    }  
                }
            }
        }
    }
}

- (IBAction)find:(id)sender {
    
    if (!findclick) {
        _findview.hidden=NO;
        findclick=YES;
    }
    else
    {
        findclick=NO;
        _findview.hidden=YES;
    }
}
-(void)closefind
{
    _findview.hidden=NO;
}
@end
