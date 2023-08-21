"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[475],{3905:(e,t,r)=>{r.d(t,{Zo:()=>l,kt:()=>h});var n=r(7294);function a(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function o(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function i(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?o(Object(r),!0).forEach((function(t){a(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):o(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function c(e,t){if(null==e)return{};var r,n,a=function(e,t){if(null==e)return{};var r,n,a={},o=Object.keys(e);for(n=0;n<o.length;n++)r=o[n],t.indexOf(r)>=0||(a[r]=e[r]);return a}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(n=0;n<o.length;n++)r=o[n],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(a[r]=e[r])}return a}var s=n.createContext({}),p=function(e){var t=n.useContext(s),r=t;return e&&(r="function"==typeof e?e(t):i(i({},t),e)),r},l=function(e){var t=p(e.components);return n.createElement(s.Provider,{value:t},e.children)},d="mdxType",m={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},u=n.forwardRef((function(e,t){var r=e.components,a=e.mdxType,o=e.originalType,s=e.parentName,l=c(e,["components","mdxType","originalType","parentName"]),d=p(r),u=a,h=d["".concat(s,".").concat(u)]||d[u]||m[u]||o;return r?n.createElement(h,i(i({ref:t},l),{},{components:r})):n.createElement(h,i({ref:t},l))}));function h(e,t){var r=arguments,a=t&&t.mdxType;if("string"==typeof e||a){var o=r.length,i=new Array(o);i[0]=u;var c={};for(var s in t)hasOwnProperty.call(t,s)&&(c[s]=t[s]);c.originalType=e,c[d]="string"==typeof e?e:a,i[1]=c;for(var p=2;p<o;p++)i[p]=r[p];return n.createElement.apply(null,i)}return n.createElement.apply(null,r)}u.displayName="MDXCreateElement"},8100:(e,t,r)=>{r.r(t),r.d(t,{assets:()=>s,contentTitle:()=>i,default:()=>m,frontMatter:()=>o,metadata:()=>c,toc:()=>p});var n=r(7462),a=(r(7294),r(3905));const o={sidebar_position:1},i="Architecture",c={unversionedId:"hierarchy/intro",id:"hierarchy/intro",title:"Architecture",description:"PeakRDL-halcpp is composed of C++ library of primitive template classes that correspond to SystemRDL components.",source:"@site/docs/hierarchy/intro.md",sourceDirName:"hierarchy",slug:"/hierarchy/intro",permalink:"/PeakRDL-halcpp/docs/hierarchy/intro",draft:!1,editUrl:"https://github.com/risto97/peakrdl-halcpp/tree/master/docs/hierarchy/intro.md",tags:[],version:"current",sidebarPosition:1,frontMatter:{sidebar_position:1},sidebar:"documentationSidebar",previous:{title:"Command-Line Arguments",permalink:"/PeakRDL-halcpp/docs/getting_started/cli"},next:{title:"Nodes",permalink:"/PeakRDL-halcpp/docs/category/nodes"}},s={},p=[],l={toc:p},d="wrapper";function m(e){let{components:t,...r}=e;return(0,a.kt)(d,(0,n.Z)({},l,r,{components:t,mdxType:"MDXLayout"}),(0,a.kt)("h1",{id:"architecture"},"Architecture"),(0,a.kt)("p",null,"PeakRDL-halcpp is composed of C++ library of primitive template classes that correspond to SystemRDL components.\nThey can be found in ",(0,a.kt)("a",{parentName:"p",href:"https://github.com/Risto97/PeakRDL-halcpp/tree/master/src/peakrdl_halcpp/include"},"src/include")),(0,a.kt)("p",null,"There you can find the following base template classes:"),(0,a.kt)("ul",null,(0,a.kt)("li",{parentName:"ul"},(0,a.kt)("a",{parentName:"li",href:"/docs/hierarchy/nodes/addrmap"},"AddrmapNode")),(0,a.kt)("li",{parentName:"ul"},(0,a.kt)("a",{parentName:"li",href:"/docs/hierarchy/nodes/reg"},"RegNode")),(0,a.kt)("li",{parentName:"ul"},(0,a.kt)("a",{parentName:"li",href:"/docs/hierarchy/nodes/field"},"FieldNode")),(0,a.kt)("li",{parentName:"ul"},(0,a.kt)("a",{parentName:"li",href:"/docs/hierarchy/nodes/mem"},"MemNode")),(0,a.kt)("li",{parentName:"ul"},(0,a.kt)("a",{parentName:"li",href:"/docs/hierarchy/nodes/arch_io"},"ArchIoNode"))),(0,a.kt)("p",null,"The C++ template classes represent the components under the same name in SystemRDL standard.\nThe hierarchy stays the same, and its made by compositions of objects inside classes."))}m.isMDXComponent=!0}}]);