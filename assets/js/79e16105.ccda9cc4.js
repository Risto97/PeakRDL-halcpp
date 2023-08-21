"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[947],{3905:(e,t,r)=>{r.d(t,{Zo:()=>d,kt:()=>u});var o=r(7294);function n(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function i(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);t&&(o=o.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,o)}return r}function a(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?i(Object(r),!0).forEach((function(t){n(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):i(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function c(e,t){if(null==e)return{};var r,o,n=function(e,t){if(null==e)return{};var r,o,n={},i=Object.keys(e);for(o=0;o<i.length;o++)r=i[o],t.indexOf(r)>=0||(n[r]=e[r]);return n}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(o=0;o<i.length;o++)r=i[o],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(n[r]=e[r])}return n}var l=o.createContext({}),p=function(e){var t=o.useContext(l),r=t;return e&&(r="function"==typeof e?e(t):a(a({},t),e)),r},d=function(e){var t=p(e.components);return o.createElement(l.Provider,{value:t},e.children)},s="mdxType",h={inlineCode:"code",wrapper:function(e){var t=e.children;return o.createElement(o.Fragment,{},t)}},m=o.forwardRef((function(e,t){var r=e.components,n=e.mdxType,i=e.originalType,l=e.parentName,d=c(e,["components","mdxType","originalType","parentName"]),s=p(r),m=n,u=s["".concat(l,".").concat(m)]||s[m]||h[m]||i;return r?o.createElement(u,a(a({ref:t},d),{},{components:r})):o.createElement(u,a({ref:t},d))}));function u(e,t){var r=arguments,n=t&&t.mdxType;if("string"==typeof e||n){var i=r.length,a=new Array(i);a[0]=m;var c={};for(var l in t)hasOwnProperty.call(t,l)&&(c[l]=t[l]);c.originalType=e,c[s]="string"==typeof e?e:n,a[1]=c;for(var p=2;p<i;p++)a[p]=r[p];return o.createElement.apply(null,a)}return o.createElement.apply(null,r)}m.displayName="MDXCreateElement"},2741:(e,t,r)=>{r.r(t),r.d(t,{assets:()=>l,contentTitle:()=>a,default:()=>h,frontMatter:()=>i,metadata:()=>c,toc:()=>p});var o=r(7462),n=(r(7294),r(3905));const i={sidebar_position:6},a="ArchIoNode",c={unversionedId:"hierarchy/nodes/arch_io/arch_io",id:"hierarchy/nodes/arch_io/arch_io",title:"ArchIoNode",description:"This node is meant to provide the memory IO operation of the platform.",source:"@site/docs/hierarchy/nodes/arch_io/arch_io.md",sourceDirName:"hierarchy/nodes/arch_io",slug:"/hierarchy/nodes/arch_io/",permalink:"/PeakRDL-halcpp/docs/hierarchy/nodes/arch_io/",draft:!1,editUrl:"https://github.com/risto97/peakrdl-halcpp/tree/master/docs/hierarchy/nodes/arch_io/arch_io.md",tags:[],version:"current",sidebarPosition:6,frontMatter:{sidebar_position:6},sidebar:"documentationSidebar",previous:{title:"MemNode",permalink:"/PeakRDL-halcpp/docs/hierarchy/nodes/mem/"},next:{title:"RegFileNode",permalink:"/PeakRDL-halcpp/docs/hierarchy/nodes/regfile/"}},l={},p=[{value:"Overriding <code>ArchIoNode</code>",id:"overriding-archionode",level:2}],d={toc:p},s="wrapper";function h(e){let{components:t,...r}=e;return(0,n.kt)(s,(0,o.Z)({},d,r,{components:t,mdxType:"MDXLayout"}),(0,n.kt)("h1",{id:"archionode"},"ArchIoNode"),(0,n.kt)("p",null,"This node is meant to provide the memory IO operation of the platform.\nIt is supposed to implement ",(0,n.kt)("inlineCode",{parentName:"p"},"write32")," and ",(0,n.kt)("inlineCode",{parentName:"p"},"read32")," methods."),(0,n.kt)("p",null,(0,n.kt)("inlineCode",{parentName:"p"},"ArchIoNode")," is meant to be inherited by a top ",(0,n.kt)("inlineCode",{parentName:"p"},"AddrmapNode"),"."),(0,n.kt)("p",null,"By default a default ",(0,n.kt)("inlineCode",{parentName:"p"},"ArchIoNode")," is provided and will be copied to the output directory.\nThe default node provides a typical memory IO operations for a CPU.\nHowever it is possible to override this node in cases of:"),(0,n.kt)("ul",null,(0,n.kt)("li",{parentName:"ul"},"Using generated halcpp drivers as a ",(0,n.kt)("inlineCode",{parentName:"li"},"UVM-RAL")," for ",(0,n.kt)("inlineCode",{parentName:"li"},"SystemC-UVM")," or ",(0,n.kt)("inlineCode",{parentName:"li"},"C++")," testbenches."),(0,n.kt)("li",{parentName:"ul"},"For debugging, where you might want to replace memory IO with console prints"),(0,n.kt)("li",{parentName:"ul"},"For Emulation, where you might want to model memory IO operations its side effects in the platform."),(0,n.kt)("li",{parentName:"ul"},"Or Simply if the provided ",(0,n.kt)("inlineCode",{parentName:"li"},"ArchIoNode")," is not adequate.")),(0,n.kt)("h2",{id:"overriding-archionode"},"Overriding ",(0,n.kt)("inlineCode",{parentName:"h2"},"ArchIoNode")),(0,n.kt)("p",null,"In order to override the default class the easiest way to do it is following:"),(0,n.kt)("pre",null,(0,n.kt)("code",{parentName:"pre",className:"language-cpp"},'#define _ARCH_IO_H_\n\nclass ArchIoNode {\npublic:\n// ... Your custom implementation\n};\n\n#include "soc_hal.h"\n')),(0,n.kt)("p",null,"The easiest solution is to define macro ",(0,n.kt)("inlineCode",{parentName:"p"},"_ARCH_IO_H_")," before including the HAL driver header file (in this case ",(0,n.kt)("inlineCode",{parentName:"p"},"soc_hal.h"),").\nAfter that you need to provide your custom implemetnation for ArchIoNode."))}h.isMDXComponent=!0}}]);