# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name objc2-core-graphics
%global full_version 0.3.2
%global pkgname objc2-core-graphics-0.3

Name:           rust-objc2-core-graphics-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "objc2-core-graphics"
License:        Zlib OR Apache-2.0 OR MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:e022c9d066895efa1345f8e33e584b9f958da2fd4cd116792e15e07e4720a807
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(objc2-core-foundation-0.3) >= 0.3.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/cgbase) = %{version}
Provides:       crate(%{pkgname}/cgdirectdisplaymetal) = %{version}
Provides:       crate(%{pkgname}/cgdirectpalette) = %{version}
Provides:       crate(%{pkgname}/cgdisplayfade) = %{version}
Provides:       crate(%{pkgname}/cgerror) = %{version}
Provides:       crate(%{pkgname}/cgitutonemapping) = %{version}
Provides:       crate(%{pkgname}/cgpdfoperatortable) = %{version}
Provides:       crate(%{pkgname}/cgwindowlevel) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/unstable-darwin-objc) = %{version}

%description
Source code for takopackized Rust crate "objc2-core-graphics"

%package     -n %{name}+cgaffinetransform
Summary:        Bindings to the CoreGraphics framework - feature "CGAffineTransform" and 8 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Provides:       crate(%{pkgname}/cgaffinetransform) = %{version}
Provides:       crate(%{pkgname}/cgfunction) = %{version}
Provides:       crate(%{pkgname}/cgpattern) = %{version}
Provides:       crate(%{pkgname}/cgpdfarray) = %{version}
Provides:       crate(%{pkgname}/cgpdfdictionary) = %{version}
Provides:       crate(%{pkgname}/cgpdfobject) = %{version}
Provides:       crate(%{pkgname}/cgpdfpage) = %{version}
Provides:       crate(%{pkgname}/cgpdfscanner) = %{version}
Provides:       crate(%{pkgname}/cgshading) = %{version}

%description -n %{name}+cgaffinetransform
This metapackage enables feature "CGAffineTransform" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CGFunction", "CGPDFArray", "CGPDFDictionary", "CGPDFObject", "CGPDFPage", "CGPDFScanner", "CGPattern", and "CGShading" features.

%package     -n %{name}+cgbitmapcontext
Summary:        Bindings to the CoreGraphics framework - feature "CGBitmapContext"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfbyteorder) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cferror) >= 0.3.2
Provides:       crate(%{pkgname}/cgbitmapcontext) = %{version}

%description -n %{name}+cgbitmapcontext
This metapackage enables feature "CGBitmapContext" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cgcolor
Summary:        Bindings to the CoreGraphics framework - feature "CGColor" and 4 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Provides:       crate(%{pkgname}/cgcolor) = %{version}
Provides:       crate(%{pkgname}/cgcontext) = %{version}
Provides:       crate(%{pkgname}/cgconvertcolordatawithformat) = %{version}
Provides:       crate(%{pkgname}/cggeometry) = %{version}
Provides:       crate(%{pkgname}/cglayer) = %{version}

%description -n %{name}+cgcolor
This metapackage enables feature "CGColor" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CGContext", "CGConvertColorDataWithFormat", "CGGeometry", and "CGLayer" features.

%package     -n %{name}+cgcolorconversioninfo
Summary:        Bindings to the CoreGraphics framework - feature "CGColorConversionInfo"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cferror) >= 0.3.2
Provides:       crate(%{pkgname}/cgcolorconversioninfo) = %{version}

%description -n %{name}+cgcolorconversioninfo
This metapackage enables feature "CGColorConversionInfo" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cgcolorspace
Summary:        Bindings to the CoreGraphics framework - feature "CGColorSpace"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdata) >= 0.3.2
Provides:       crate(%{pkgname}/cgcolorspace) = %{version}

%description -n %{name}+cgcolorspace
This metapackage enables feature "CGColorSpace" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cgdataconsumer
Summary:        Bindings to the CoreGraphics framework - feature "CGDataConsumer" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfdata) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfurl) >= 0.3.2
Provides:       crate(%{pkgname}/cgdataconsumer) = %{version}
Provides:       crate(%{pkgname}/cgdataprovider) = %{version}

%description -n %{name}+cgdataconsumer
This metapackage enables feature "CGDataConsumer" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CGDataProvider" feature.

%package     -n %{name}+cgdirectdisplay
Summary:        Bindings to the CoreGraphics framework - feature "CGDirectDisplay"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfarray) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Provides:       crate(%{pkgname}/cgdirectdisplay) = %{version}

%description -n %{name}+cgdirectdisplay
This metapackage enables feature "CGDirectDisplay" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cgdisplayconfiguration
Summary:        Bindings to the CoreGraphics framework - feature "CGDisplayConfiguration"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Provides:       crate(%{pkgname}/cgdisplayconfiguration) = %{version}

%description -n %{name}+cgdisplayconfiguration
This metapackage enables feature "CGDisplayConfiguration" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cgdisplaystream
Summary:        Bindings to the CoreGraphics framework - feature "CGDisplayStream"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfrunloop) >= 0.3.2
Provides:       crate(%{pkgname}/cgdisplaystream) = %{version}

%description -n %{name}+cgdisplaystream
This metapackage enables feature "CGDisplayStream" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cgexrtonemappinggamma
Summary:        Bindings to the CoreGraphics framework - feature "CGEXRToneMappingGamma" and 3 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Provides:       crate(%{pkgname}/cgexrtonemappinggamma) = %{version}
Provides:       crate(%{pkgname}/cgpsconverter) = %{version}
Provides:       crate(%{pkgname}/cgsession) = %{version}
Provides:       crate(%{pkgname}/cgtonemapping) = %{version}

%description -n %{name}+cgexrtonemappinggamma
This metapackage enables feature "CGEXRToneMappingGamma" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CGPSConverter", "CGSession", and "CGToneMapping" features.

%package     -n %{name}+cgevent
Summary:        Bindings to the CoreGraphics framework - feature "CGEvent"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdata) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfmachport) >= 0.3.2
Provides:       crate(%{pkgname}/cgevent) = %{version}

%description -n %{name}+cgevent
This metapackage enables feature "CGEvent" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cgeventsource
Summary:        Bindings to the CoreGraphics framework - feature "CGEventSource" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfdate) >= 0.3.2
Provides:       crate(%{pkgname}/cgeventsource) = %{version}
Provides:       crate(%{pkgname}/cgpdfstring) = %{version}

%description -n %{name}+cgeventsource
This metapackage enables feature "CGEventSource" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CGPDFString" feature.

%package     -n %{name}+cgfont
Summary:        Bindings to the CoreGraphics framework - feature "CGFont"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfarray) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdata) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Provides:       crate(%{pkgname}/cgfont) = %{version}

%description -n %{name}+cgfont
This metapackage enables feature "CGFont" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cggradient
Summary:        Bindings to the CoreGraphics framework - feature "CGGradient" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfarray) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Provides:       crate(%{pkgname}/cggradient) = %{version}
Provides:       crate(%{pkgname}/cgwindow) = %{version}

%description -n %{name}+cggradient
This metapackage enables feature "CGGradient" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CGWindow" feature.

%package     -n %{name}+cgimage
Summary:        Bindings to the CoreGraphics framework - feature "CGImage"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Provides:       crate(%{pkgname}/cgimage) = %{version}

%description -n %{name}+cgimage
This metapackage enables feature "CGImage" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cgpdfcontentstream
Summary:        Bindings to the CoreGraphics framework - feature "CGPDFContentStream"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfarray) >= 0.3.2
Provides:       crate(%{pkgname}/cgpdfcontentstream) = %{version}

%description -n %{name}+cgpdfcontentstream
This metapackage enables feature "CGPDFContentStream" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cgpdfcontext
Summary:        Bindings to the CoreGraphics framework - feature "CGPDFContext"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdata) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfurl) >= 0.3.2
Provides:       crate(%{pkgname}/cgpdfcontext) = %{version}

%description -n %{name}+cgpdfcontext
This metapackage enables feature "CGPDFContext" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cgpdfdocument
Summary:        Bindings to the CoreGraphics framework - feature "CGPDFDocument"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdictionary) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfurl) >= 0.3.2
Provides:       crate(%{pkgname}/cgpdfdocument) = %{version}

%description -n %{name}+cgpdfdocument
This metapackage enables feature "CGPDFDocument" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cgpdfstream
Summary:        Bindings to the CoreGraphics framework - feature "CGPDFStream" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfdata) >= 0.3.2
Provides:       crate(%{pkgname}/cgpdfstream) = %{version}
Provides:       crate(%{pkgname}/cgrenderingbufferprovider) = %{version}

%description -n %{name}+cgpdfstream
This metapackage enables feature "CGPDFStream" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CGRenderingBufferProvider" feature.

%package     -n %{name}+cgpath
Summary:        Bindings to the CoreGraphics framework - feature "CGPath"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfarray) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Provides:       crate(%{pkgname}/cgpath) = %{version}

%description -n %{name}+cgpath
This metapackage enables feature "CGPath" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cgremoteoperation
Summary:        Bindings to the CoreGraphics framework - feature "CGRemoteOperation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdate) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfmachport) >= 0.3.2
Provides:       crate(%{pkgname}/cgremoteoperation) = %{version}

%description -n %{name}+cgremoteoperation
This metapackage enables feature "CGRemoteOperation" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bitflags
Summary:        Bindings to the CoreGraphics framework - feature "bitflags" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bitflags-2/std) >= 2.5.0
Provides:       crate(%{pkgname}/bitflags) = %{version}
Provides:       crate(%{pkgname}/cgeventtypes) = %{version}

%description -n %{name}+bitflags
This metapackage enables feature "bitflags" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CGEventTypes" feature.

%package     -n %{name}+block2
Summary:        Bindings to the CoreGraphics framework - feature "block2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block2-0.6/alloc) >= 0.6.1
Provides:       crate(%{pkgname}/block2) = %{version}

%description -n %{name}+block2
This metapackage enables feature "block2" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Bindings to the CoreGraphics framework - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(%{pkgname}/block2) = %{version}
Requires:       crate(%{pkgname}/cgaffinetransform) = %{version}
Requires:       crate(%{pkgname}/cgbase) = %{version}
Requires:       crate(%{pkgname}/cgbitmapcontext) = %{version}
Requires:       crate(%{pkgname}/cgcolor) = %{version}
Requires:       crate(%{pkgname}/cgcolorconversioninfo) = %{version}
Requires:       crate(%{pkgname}/cgcolorspace) = %{version}
Requires:       crate(%{pkgname}/cgcontext) = %{version}
Requires:       crate(%{pkgname}/cgconvertcolordatawithformat) = %{version}
Requires:       crate(%{pkgname}/cgdataconsumer) = %{version}
Requires:       crate(%{pkgname}/cgdataprovider) = %{version}
Requires:       crate(%{pkgname}/cgdirectdisplay) = %{version}
Requires:       crate(%{pkgname}/cgdirectdisplaymetal) = %{version}
Requires:       crate(%{pkgname}/cgdirectpalette) = %{version}
Requires:       crate(%{pkgname}/cgdisplayconfiguration) = %{version}
Requires:       crate(%{pkgname}/cgdisplayfade) = %{version}
Requires:       crate(%{pkgname}/cgdisplaystream) = %{version}
Requires:       crate(%{pkgname}/cgerror) = %{version}
Requires:       crate(%{pkgname}/cgevent) = %{version}
Requires:       crate(%{pkgname}/cgeventsource) = %{version}
Requires:       crate(%{pkgname}/cgeventtypes) = %{version}
Requires:       crate(%{pkgname}/cgexrtonemappinggamma) = %{version}
Requires:       crate(%{pkgname}/cgfont) = %{version}
Requires:       crate(%{pkgname}/cgfunction) = %{version}
Requires:       crate(%{pkgname}/cggeometry) = %{version}
Requires:       crate(%{pkgname}/cggradient) = %{version}
Requires:       crate(%{pkgname}/cgimage) = %{version}
Requires:       crate(%{pkgname}/cgitutonemapping) = %{version}
Requires:       crate(%{pkgname}/cglayer) = %{version}
Requires:       crate(%{pkgname}/cgpath) = %{version}
Requires:       crate(%{pkgname}/cgpattern) = %{version}
Requires:       crate(%{pkgname}/cgpdfarray) = %{version}
Requires:       crate(%{pkgname}/cgpdfcontentstream) = %{version}
Requires:       crate(%{pkgname}/cgpdfcontext) = %{version}
Requires:       crate(%{pkgname}/cgpdfdictionary) = %{version}
Requires:       crate(%{pkgname}/cgpdfdocument) = %{version}
Requires:       crate(%{pkgname}/cgpdfobject) = %{version}
Requires:       crate(%{pkgname}/cgpdfoperatortable) = %{version}
Requires:       crate(%{pkgname}/cgpdfpage) = %{version}
Requires:       crate(%{pkgname}/cgpdfscanner) = %{version}
Requires:       crate(%{pkgname}/cgpdfstream) = %{version}
Requires:       crate(%{pkgname}/cgpdfstring) = %{version}
Requires:       crate(%{pkgname}/cgpsconverter) = %{version}
Requires:       crate(%{pkgname}/cgremoteoperation) = %{version}
Requires:       crate(%{pkgname}/cgrenderingbufferprovider) = %{version}
Requires:       crate(%{pkgname}/cgsession) = %{version}
Requires:       crate(%{pkgname}/cgshading) = %{version}
Requires:       crate(%{pkgname}/cgtonemapping) = %{version}
Requires:       crate(%{pkgname}/cgwindow) = %{version}
Requires:       crate(%{pkgname}/cgwindowlevel) = %{version}
Requires:       crate(%{pkgname}/dispatch2) = %{version}
Requires:       crate(%{pkgname}/libc) = %{version}
Requires:       crate(%{pkgname}/objc2) = %{version}
Requires:       crate(%{pkgname}/objc2-metal) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dispatch2
Summary:        Bindings to the CoreGraphics framework - feature "dispatch2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(dispatch2-0.3/alloc) >= 0.3.0
Provides:       crate(%{pkgname}/dispatch2) = %{version}

%description -n %{name}+dispatch2
This metapackage enables feature "dispatch2" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libc
Summary:        Bindings to the CoreGraphics framework - feature "libc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2) >= 0.2.80
Provides:       crate(%{pkgname}/libc) = %{version}

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2
Summary:        Bindings to the CoreGraphics framework - feature "objc2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(dispatch2-0.3/alloc) >= 0.3.0
Requires:       crate(dispatch2-0.3/objc2) >= 0.3.0
Requires:       crate(objc2-0.6/std) >= 0.6.2
Requires:       crate(objc2-core-foundation-0.3/objc2) >= 0.3.2
Requires:       crate(objc2-io-surface-0.3/iosurfaceref) >= 0.3.2
Requires:       crate(objc2-io-surface-0.3/objc2) >= 0.3.2
Provides:       crate(%{pkgname}/objc2) = %{version}

%description -n %{name}+objc2
This metapackage enables feature "objc2" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-io-surface
Summary:        Bindings to the CoreGraphics framework - feature "objc2-io-surface"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-io-surface-0.3/iosurfaceref) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-io-surface) = %{version}

%description -n %{name}+objc2-io-surface
This metapackage enables feature "objc2-io-surface" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-metal
Summary:        Bindings to the CoreGraphics framework - feature "objc2-metal"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-metal-0.3/mtldevice) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-metal) = %{version}

%description -n %{name}+objc2-metal
This metapackage enables feature "objc2-metal" for the Rust objc2-core-graphics crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
