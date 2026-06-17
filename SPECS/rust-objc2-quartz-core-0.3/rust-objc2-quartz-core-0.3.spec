# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name objc2-quartz-core
%global full_version 0.3.2
%global pkgname objc2-quartz-core-0.3

Name:           rust-objc2-quartz-core-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "objc2-quartz-core"
License:        Zlib OR Apache-2.0 OR MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:96c1358452b371bf9f104e21ec536d37a650eb10f7ee379fff67d2e08d537f1f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(objc2-0.6/std) >= 0.6.2
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/cabase) = %{version}
Provides:       crate(%{pkgname}/caeagllayer) = %{version}
Provides:       crate(%{pkgname}/caframeraterange) = %{version}
Provides:       crate(%{pkgname}/caremotelayerclient) = %{version}
Provides:       crate(%{pkgname}/caremotelayerserver) = %{version}
Provides:       crate(%{pkgname}/coreanimation) = %{version}
Provides:       crate(%{pkgname}/gnustep-1-7) = %{version}
Provides:       crate(%{pkgname}/gnustep-1-8) = %{version}
Provides:       crate(%{pkgname}/gnustep-1-9) = %{version}
Provides:       crate(%{pkgname}/gnustep-2-0) = %{version}
Provides:       crate(%{pkgname}/gnustep-2-1) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/unstable-darwin-objc) = %{version}

%description
Source code for takopackized Rust crate "objc2-quartz-core"

%package     -n %{name}+caanimation
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "CAAnimation" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsvalue) >= 0.3.2
Provides:       crate(%{pkgname}/caanimation) = %{version}
Provides:       crate(%{pkgname}/cagradientlayer) = %{version}
Provides:       crate(%{pkgname}/cashapelayer) = %{version}

%description -n %{name}+caanimation
This metapackage enables feature "CAAnimation" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CAGradientLayer", and "CAShapeLayer" features.

%package     -n %{name}+caconstraintlayoutmanager
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "CAConstraintLayoutManager" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/caconstraintlayoutmanager) = %{version}
Provides:       crate(%{pkgname}/caemitterlayer) = %{version}

%description -n %{name}+caconstraintlayoutmanager
This metapackage enables feature "CAConstraintLayoutManager" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CAEmitterLayer" feature.

%package     -n %{name}+cadisplaylink
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "CADisplayLink" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobjcruntime) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsrunloop) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/cadisplaylink) = %{version}
Provides:       crate(%{pkgname}/cametaldisplaylink) = %{version}

%description -n %{name}+cadisplaylink
This metapackage enables feature "CADisplayLink" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CAMetalDisplayLink" feature.

%package     -n %{name}+caedrmetadata
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "CAEDRMetadata"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/caedrmetadata) = %{version}

%description -n %{name}+caedrmetadata
This metapackage enables feature "CAEDRMetadata" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+caemittercell
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "CAEmitterCell"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/caemittercell) = %{version}

%description -n %{name}+caemittercell
This metapackage enables feature "CAEmitterCell" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+calayer
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "CALayer"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnull) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/calayer) = %{version}

%description -n %{name}+calayer
This metapackage enables feature "CALayer" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+camediatiming
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "CAMediaTiming" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/camediatiming) = %{version}
Provides:       crate(%{pkgname}/catransaction) = %{version}

%description -n %{name}+camediatiming
This metapackage enables feature "CAMediaTiming" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CATransaction" feature.

%package     -n %{name}+camediatimingfunction
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "CAMediaTimingFunction" and 3 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/camediatimingfunction) = %{version}
Provides:       crate(%{pkgname}/cascrolllayer) = %{version}
Provides:       crate(%{pkgname}/catextlayer) = %{version}
Provides:       crate(%{pkgname}/cavaluefunction) = %{version}

%description -n %{name}+camediatimingfunction
This metapackage enables feature "CAMediaTimingFunction" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CAScrollLayer", "CATextLayer", and "CAValueFunction" features.

%package     -n %{name}+cametallayer
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "CAMetalLayer"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/cametallayer) = %{version}

%description -n %{name}+cametallayer
This metapackage enables feature "CAMetalLayer" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+caopengllayer
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "CAOpenGLLayer" and 3 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/caopengllayer) = %{version}
Provides:       crate(%{pkgname}/careplicatorlayer) = %{version}
Provides:       crate(%{pkgname}/catiledlayer) = %{version}
Provides:       crate(%{pkgname}/catransformlayer) = %{version}

%description -n %{name}+caopengllayer
This metapackage enables feature "CAOpenGLLayer" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CAReplicatorLayer", "CATiledLayer", and "CATransformLayer" features.

%package     -n %{name}+carenderer
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "CARenderer"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/carenderer) = %{version}

%description -n %{name}+carenderer
This metapackage enables feature "CARenderer" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+catransform3d
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "CATransform3D"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsvalue) >= 0.3.2
Provides:       crate(%{pkgname}/catransform3d) = %{version}

%description -n %{name}+catransform3d
This metapackage enables feature "CATransform3D" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bitflags
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "bitflags"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bitflags-2/std) >= 2.5.0
Provides:       crate(%{pkgname}/bitflags) = %{version}

%description -n %{name}+bitflags
This metapackage enables feature "bitflags" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+block2
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "block2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block2-0.6/alloc) >= 0.6.1
Provides:       crate(%{pkgname}/block2) = %{version}

%description -n %{name}+block2
This metapackage enables feature "block2" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(%{pkgname}/block2) = %{version}
Requires:       crate(%{pkgname}/caanimation) = %{version}
Requires:       crate(%{pkgname}/cabase) = %{version}
Requires:       crate(%{pkgname}/caconstraintlayoutmanager) = %{version}
Requires:       crate(%{pkgname}/cadisplaylink) = %{version}
Requires:       crate(%{pkgname}/caeagllayer) = %{version}
Requires:       crate(%{pkgname}/caedrmetadata) = %{version}
Requires:       crate(%{pkgname}/caemittercell) = %{version}
Requires:       crate(%{pkgname}/caemitterlayer) = %{version}
Requires:       crate(%{pkgname}/caframeraterange) = %{version}
Requires:       crate(%{pkgname}/cagradientlayer) = %{version}
Requires:       crate(%{pkgname}/calayer) = %{version}
Requires:       crate(%{pkgname}/camediatiming) = %{version}
Requires:       crate(%{pkgname}/camediatimingfunction) = %{version}
Requires:       crate(%{pkgname}/cametaldisplaylink) = %{version}
Requires:       crate(%{pkgname}/cametallayer) = %{version}
Requires:       crate(%{pkgname}/caopengllayer) = %{version}
Requires:       crate(%{pkgname}/caremotelayerclient) = %{version}
Requires:       crate(%{pkgname}/caremotelayerserver) = %{version}
Requires:       crate(%{pkgname}/carenderer) = %{version}
Requires:       crate(%{pkgname}/careplicatorlayer) = %{version}
Requires:       crate(%{pkgname}/cascrolllayer) = %{version}
Requires:       crate(%{pkgname}/cashapelayer) = %{version}
Requires:       crate(%{pkgname}/catextlayer) = %{version}
Requires:       crate(%{pkgname}/catiledlayer) = %{version}
Requires:       crate(%{pkgname}/catransaction) = %{version}
Requires:       crate(%{pkgname}/catransform3d) = %{version}
Requires:       crate(%{pkgname}/catransformlayer) = %{version}
Requires:       crate(%{pkgname}/cavaluefunction) = %{version}
Requires:       crate(%{pkgname}/coreanimation) = %{version}
Requires:       crate(%{pkgname}/libc) = %{version}
Requires:       crate(%{pkgname}/objc2-core-foundation) = %{version}
Requires:       crate(%{pkgname}/objc2-core-graphics) = %{version}
Requires:       crate(%{pkgname}/objc2-core-video) = %{version}
Requires:       crate(%{pkgname}/objc2-metal) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libc
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "libc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2) >= 0.2.80
Provides:       crate(%{pkgname}/libc) = %{version}

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-core-foundation
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "objc2-core-foundation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdate) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/objc2) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-core-foundation) = %{version}

%description -n %{name}+objc2-core-foundation
This metapackage enables feature "objc2-core-foundation" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-core-graphics
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "objc2-core-graphics"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-graphics-0.3/cgcolor) >= 0.3.2
Requires:       crate(objc2-core-graphics-0.3/cgcolorspace) >= 0.3.2
Requires:       crate(objc2-core-graphics-0.3/cgcontext) >= 0.3.2
Requires:       crate(objc2-core-graphics-0.3/cgpath) >= 0.3.2
Requires:       crate(objc2-core-graphics-0.3/objc2) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-core-graphics) = %{version}

%description -n %{name}+objc2-core-graphics
This metapackage enables feature "objc2-core-graphics" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-core-video
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "objc2-core-video"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-video-0.3/cvbase) >= 0.3.2
Requires:       crate(objc2-core-video-0.3/objc2) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-core-video) = %{version}

%description -n %{name}+objc2-core-video
This metapackage enables feature "objc2-core-video" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-metal
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "objc2-metal"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-metal-0.3/mtlallocation) >= 0.3.2
Requires:       crate(objc2-metal-0.3/mtldevice) >= 0.3.2
Requires:       crate(objc2-metal-0.3/mtldrawable) >= 0.3.2
Requires:       crate(objc2-metal-0.3/mtlpixelformat) >= 0.3.2
Requires:       crate(objc2-metal-0.3/mtlresidencyset) >= 0.3.2
Requires:       crate(objc2-metal-0.3/mtlresource) >= 0.3.2
Requires:       crate(objc2-metal-0.3/mtltexture) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-metal) = %{version}

%description -n %{name}+objc2-metal
This metapackage enables feature "objc2-metal" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-open-gl
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "objc2-open-gl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-open-gl-0.3/cgltypes) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-open-gl) = %{version}

%description -n %{name}+objc2-open-gl
This metapackage enables feature "objc2-open-gl" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
