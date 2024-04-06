"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[146],{5680:(e,t,a)=>{a.d(t,{xA:()=>d,yg:()=>u});var n=a(6540);function r(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function l(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,n)}return a}function i(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?l(Object(a),!0).forEach((function(t){r(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):l(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function p(e,t){if(null==e)return{};var a,n,r=function(e,t){if(null==e)return{};var a,n,r={},l=Object.keys(e);for(n=0;n<l.length;n++)a=l[n],t.indexOf(a)>=0||(r[a]=e[a]);return r}(e,t);if(Object.getOwnPropertySymbols){var l=Object.getOwnPropertySymbols(e);for(n=0;n<l.length;n++)a=l[n],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(r[a]=e[a])}return r}var g=n.createContext({}),o=function(e){var t=n.useContext(g),a=t;return e&&(a="function"==typeof e?e(t):i(i({},t),e)),a},d=function(e){var t=o(e.components);return n.createElement(g.Provider,{value:t},e.children)},m="mdxType",y={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},s=n.forwardRef((function(e,t){var a=e.components,r=e.mdxType,l=e.originalType,g=e.parentName,d=p(e,["components","mdxType","originalType","parentName"]),m=o(a),s=r,u=m["".concat(g,".").concat(s)]||m[s]||y[s]||l;return a?n.createElement(u,i(i({ref:t},d),{},{components:a})):n.createElement(u,i({ref:t},d))}));function u(e,t){var a=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var l=a.length,i=new Array(l);i[0]=s;var p={};for(var g in t)hasOwnProperty.call(t,g)&&(p[g]=t[g]);p.originalType=e,p[m]="string"==typeof e?e:r,i[1]=p;for(var o=2;o<l;o++)i[o]=a[o];return n.createElement.apply(null,i)}return n.createElement.apply(null,a)}s.displayName="MDXCreateElement"},2457:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>g,contentTitle:()=>i,default:()=>y,frontMatter:()=>l,metadata:()=>p,toc:()=>o});var n=a(8168),r=(a(6540),a(5680));const l={sidebar_position:3},i="Command-Line Arguments",p={unversionedId:"getting_started/cli",id:"getting_started/cli",title:"Command-Line Arguments",description:"Usage",source:"@site/docs/getting_started/cli.md",sourceDirName:"getting_started",slug:"/getting_started/cli",permalink:"/PeakRDL-halcpp/docs/getting_started/cli",draft:!1,editUrl:"https://github.com/risto97/peakrdl-halcpp/tree/master/docs/getting_started/cli.md",tags:[],version:"current",sidebarPosition:3,frontMatter:{sidebar_position:3},sidebar:"documentationSidebar",previous:{title:"Example",permalink:"/PeakRDL-halcpp/docs/getting_started/example"},next:{title:"Architecture",permalink:"/PeakRDL-halcpp/docs/hierarchy/intro"}},g={},o=[{value:"Usage",id:"usage",level:2},{value:"Arguments",id:"arguments",level:2},{value:"<code>-h</code> <code>--help</code>",id:"_h___help",level:3},{value:"<code>FILE</code>",id:"FILE",level:3},{value:"<code>-I</code>",id:"_I",level:3},{value:"<code>-t</code> <code>--top</code>",id:"_t___top",level:3},{value:"<code>--rename</code>",id:"__rename",level:3},{value:"<code>-P</code>",id:"_P",level:3},{value:"<code>--remap-state</code>",id:"__remap_state",level:3},{value:"<code>-o</code>",id:"_o",level:3},{value:"<code>--ext</code>",id:"__ext",level:3},{value:"<code>--list-files</code>",id:"__list_files",level:3},{value:"<code>--skip-buses</code>",id:"__skip_buses",level:3}],d={toc:o},m="wrapper";function y(e){let{components:t,...a}=e;return(0,r.yg)(m,(0,n.A)({},d,a,{components:t,mdxType:"MDXLayout"}),(0,r.yg)("h1",{id:"command-line-arguments"},"Command-Line Arguments"),(0,r.yg)("h2",{id:"usage"},"Usage"),(0,r.yg)("pre",null,(0,r.yg)("code",{parentName:"pre"},"peakrdl halcpp [-h] [-I INCDIR] [-t TOP] [--rename INST_NAME]\n                    [-P PARAMETER=VALUE] -o OUTPUT [--ext [EXT [EXT ...]]]\n                    [--list-files] [--skip-buses] [-f FILE] [--peakrdl-cfg CFG]\n                    FILE [FILE ...]\n")),(0,r.yg)("h2",{id:"arguments"},"Arguments"),(0,r.yg)("table",null,(0,r.yg)("thead",{parentName:"table"},(0,r.yg)("tr",{parentName:"thead"},(0,r.yg)("th",{parentName:"tr",align:null},"Argument"),(0,r.yg)("th",{parentName:"tr",align:null},"Type"),(0,r.yg)("th",{parentName:"tr",align:null},"Nargs"),(0,r.yg)("th",{parentName:"tr",align:null},"Group"))),(0,r.yg)("tbody",{parentName:"table"},(0,r.yg)("tr",{parentName:"tbody"},(0,r.yg)("td",{parentName:"tr",align:null},(0,r.yg)("a",{parentName:"td",href:"#FILE"},(0,r.yg)("inlineCode",{parentName:"a"},"FILE"))),(0,r.yg)("td",{parentName:"tr",align:null},"Positional"),(0,r.yg)("td",{parentName:"tr",align:null},"+"),(0,r.yg)("td",{parentName:"tr",align:null},"compilation args")),(0,r.yg)("tr",{parentName:"tbody"},(0,r.yg)("td",{parentName:"tr",align:null},(0,r.yg)("a",{parentName:"td",href:"#_h___help"},(0,r.yg)("inlineCode",{parentName:"a"},"-h")," ",(0,r.yg)("inlineCode",{parentName:"a"},"--help"))),(0,r.yg)("td",{parentName:"tr",align:null},"Option"),(0,r.yg)("td",{parentName:"tr",align:null},"0"),(0,r.yg)("td",{parentName:"tr",align:null},"optional arguments")),(0,r.yg)("tr",{parentName:"tbody"},(0,r.yg)("td",{parentName:"tr",align:null},(0,r.yg)("a",{parentName:"td",href:"#_I"},(0,r.yg)("inlineCode",{parentName:"a"},"-I"))),(0,r.yg)("td",{parentName:"tr",align:null},"Option"),(0,r.yg)("td",{parentName:"tr",align:null},"1"),(0,r.yg)("td",{parentName:"tr",align:null},"compilation args")),(0,r.yg)("tr",{parentName:"tbody"},(0,r.yg)("td",{parentName:"tr",align:null},(0,r.yg)("a",{parentName:"td",href:"#_t___top"},(0,r.yg)("inlineCode",{parentName:"a"},"-t")," ",(0,r.yg)("inlineCode",{parentName:"a"},"--top"))),(0,r.yg)("td",{parentName:"tr",align:null},"Option"),(0,r.yg)("td",{parentName:"tr",align:null},"1"),(0,r.yg)("td",{parentName:"tr",align:null},"compilation args")),(0,r.yg)("tr",{parentName:"tbody"},(0,r.yg)("td",{parentName:"tr",align:null},(0,r.yg)("a",{parentName:"td",href:"#__rename"},(0,r.yg)("inlineCode",{parentName:"a"},"--rename"))),(0,r.yg)("td",{parentName:"tr",align:null},"Option"),(0,r.yg)("td",{parentName:"tr",align:null},"1"),(0,r.yg)("td",{parentName:"tr",align:null},"compilation args")),(0,r.yg)("tr",{parentName:"tbody"},(0,r.yg)("td",{parentName:"tr",align:null},(0,r.yg)("a",{parentName:"td",href:"#_P"},(0,r.yg)("inlineCode",{parentName:"a"},"-P"))),(0,r.yg)("td",{parentName:"tr",align:null},"Option"),(0,r.yg)("td",{parentName:"tr",align:null},"1"),(0,r.yg)("td",{parentName:"tr",align:null},"compilation args")),(0,r.yg)("tr",{parentName:"tbody"},(0,r.yg)("td",{parentName:"tr",align:null},(0,r.yg)("a",{parentName:"td",href:"#__remap_state"},(0,r.yg)("inlineCode",{parentName:"a"},"--remap-state"))),(0,r.yg)("td",{parentName:"tr",align:null},"Option"),(0,r.yg)("td",{parentName:"tr",align:null},"1"),(0,r.yg)("td",{parentName:"tr",align:null},"ip-xact importer args")),(0,r.yg)("tr",{parentName:"tbody"},(0,r.yg)("td",{parentName:"tr",align:null},(0,r.yg)("a",{parentName:"td",href:"#_o"},(0,r.yg)("inlineCode",{parentName:"a"},"-o"))),(0,r.yg)("td",{parentName:"tr",align:null},"Option"),(0,r.yg)("td",{parentName:"tr",align:null},"1"),(0,r.yg)("td",{parentName:"tr",align:null},"exporter args")),(0,r.yg)("tr",{parentName:"tbody"},(0,r.yg)("td",{parentName:"tr",align:null},(0,r.yg)("a",{parentName:"td",href:"#__ext"},(0,r.yg)("inlineCode",{parentName:"a"},"--ext"))),(0,r.yg)("td",{parentName:"tr",align:null},"Option"),(0,r.yg)("td",{parentName:"tr",align:null},"*"),(0,r.yg)("td",{parentName:"tr",align:null},"exporter args")),(0,r.yg)("tr",{parentName:"tbody"},(0,r.yg)("td",{parentName:"tr",align:null},(0,r.yg)("a",{parentName:"td",href:"#__list_files"},(0,r.yg)("inlineCode",{parentName:"a"},"--list-files"))),(0,r.yg)("td",{parentName:"tr",align:null},"Option"),(0,r.yg)("td",{parentName:"tr",align:null},"0"),(0,r.yg)("td",{parentName:"tr",align:null},"exporter args")),(0,r.yg)("tr",{parentName:"tbody"},(0,r.yg)("td",{parentName:"tr",align:null},(0,r.yg)("a",{parentName:"td",href:"#__skip_buses"},(0,r.yg)("inlineCode",{parentName:"a"},"--skip-buses"))),(0,r.yg)("td",{parentName:"tr",align:null},"Option"),(0,r.yg)("td",{parentName:"tr",align:null},"0"),(0,r.yg)("td",{parentName:"tr",align:null},"exporter args")))),(0,r.yg)("h3",{id:"_h___help"},(0,r.yg)("inlineCode",{parentName:"h3"},"-h")," ",(0,r.yg)("inlineCode",{parentName:"h3"},"--help")),(0,r.yg)("p",null,"show this help message and exit"),(0,r.yg)("h3",{id:"FILE"},(0,r.yg)("inlineCode",{parentName:"h3"},"FILE")),(0,r.yg)("p",null,"One or more input files"),(0,r.yg)("h3",{id:"_I"},(0,r.yg)("inlineCode",{parentName:"h3"},"-I")),(0,r.yg)("p",null,'Search directory for files included with `include "filename"'),(0,r.yg)("h3",{id:"_t___top"},(0,r.yg)("inlineCode",{parentName:"h3"},"-t")," ",(0,r.yg)("inlineCode",{parentName:"h3"},"--top")),(0,r.yg)("p",null,"Explicitly choose which addrmap  in the root namespace will be the top-level component. If unset, The last addrmap defined will be chosen"),(0,r.yg)("h3",{id:"__rename"},(0,r.yg)("inlineCode",{parentName:"h3"},"--rename")),(0,r.yg)("p",null,"Overrides the top-component's instantiated name. By default, the instantiated name is the same as the component's type name"),(0,r.yg)("h3",{id:"_P"},(0,r.yg)("inlineCode",{parentName:"h3"},"-P")),(0,r.yg)("p",null,"Specify value for a top-level SystemRDL parameter"),(0,r.yg)("h3",{id:"__remap_state"},(0,r.yg)("inlineCode",{parentName:"h3"},"--remap-state")),(0,r.yg)("p",null,"Optional remapState string that is used to select memoryRemap regions that are tagged under a specific remap state."),(0,r.yg)("h3",{id:"_o"},(0,r.yg)("inlineCode",{parentName:"h3"},"-o")),(0,r.yg)("p",null,"Output path"),(0,r.yg)("h3",{id:"__ext"},(0,r.yg)("inlineCode",{parentName:"h3"},"--ext")),(0,r.yg)("p",null,"list of addrmap modules that have implemented {name}_EXT class in {name}_ext.h header file, used for extending functionality"),(0,r.yg)("h3",{id:"__list_files"},(0,r.yg)("inlineCode",{parentName:"h3"},"--list-files")),(0,r.yg)("p",null,"Dont generate files, but instead just list the files that will be generated, and external files that need to be included"),(0,r.yg)("h3",{id:"__skip_buses"},(0,r.yg)("inlineCode",{parentName:"h3"},"--skip-buses")),(0,r.yg)("p",null,"By default the SystemRDL hierarchy is preserved but it can be simplified by removing buses (i.e., addrmap containing only addrmaps, not registers). This is achieved by passing the --skip-buses flag."))}y.isMDXComponent=!0}}]);