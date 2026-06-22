# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name objc2-quartz-core
%global full_version 0.2.2
%global pkgname objc2-quartz-core-0.2

Name:           rust-objc2-quartz-core-0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Rust crate "objc2-quartz-core"
License:        MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:e42bee7bff906b14b167da2bac5efe6b6a07e6f7c0a21a7308d40c960242dc7a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(objc2-0.5) >= 0.5.2
Requires:       crate(objc2-foundation-0.2) >= 0.2.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/apple) = %{version}
Provides:       crate(%{pkgname}/cabase) = %{version}
Provides:       crate(%{pkgname}/caframeraterange) = %{version}
Provides:       crate(%{pkgname}/caopengllayer) = %{version}
Provides:       crate(%{pkgname}/caremotelayerclient) = %{version}
Provides:       crate(%{pkgname}/caremotelayerserver) = %{version}
Provides:       crate(%{pkgname}/coreanimation) = %{version}
Provides:       crate(%{pkgname}/coreimage) = %{version}
Provides:       crate(%{pkgname}/corevideo) = %{version}
Provides:       crate(%{pkgname}/gnustep-1-7) = %{version}
Provides:       crate(%{pkgname}/gnustep-1-8) = %{version}
Provides:       crate(%{pkgname}/gnustep-1-9) = %{version}
Provides:       crate(%{pkgname}/gnustep-2-0) = %{version}
Provides:       crate(%{pkgname}/gnustep-2-1) = %{version}

%description
Source code for takopackized Rust crate "objc2-quartz-core"

%package     -n %{name}+caanimation
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "CAAnimation" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsvalue) >= 0.2.2
Provides:       crate(%{pkgname}/caanimation) = %{version}
Provides:       crate(%{pkgname}/cagradientlayer) = %{version}
Provides:       crate(%{pkgname}/cashapelayer) = %{version}

%description -n %{name}+caanimation
This metapackage enables feature "CAAnimation" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CAGradientLayer", and "CAShapeLayer" features.

%package     -n %{name}+caconstraintlayoutmanager
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "CAConstraintLayoutManager" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/caconstraintlayoutmanager) = %{version}
Provides:       crate(%{pkgname}/caemitterlayer) = %{version}

%description -n %{name}+caconstraintlayoutmanager
This metapackage enables feature "CAConstraintLayoutManager" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CAEmitterLayer" feature.

%package     -n %{name}+cadisplaylink
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "CADisplayLink"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsobjcruntime) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsrunloop) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/cadisplaylink) = %{version}

%description -n %{name}+cadisplaylink
This metapackage enables feature "CADisplayLink" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+caedrmetadata
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "CAEDRMetadata"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Provides:       crate(%{pkgname}/caedrmetadata) = %{version}

%description -n %{name}+caedrmetadata
This metapackage enables feature "CAEDRMetadata" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+caemittercell
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "CAEmitterCell"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/caemittercell) = %{version}

%description -n %{name}+caemittercell
This metapackage enables feature "CAEmitterCell" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+calayer
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "CALayer"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnull) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/calayer) = %{version}

%description -n %{name}+calayer
This metapackage enables feature "CALayer" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+camediatiming
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "CAMediaTiming" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/camediatiming) = %{version}
Provides:       crate(%{pkgname}/catransaction) = %{version}

%description -n %{name}+camediatiming
This metapackage enables feature "CAMediaTiming" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CATransaction" feature.

%package     -n %{name}+camediatimingfunction
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "CAMediaTimingFunction" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/camediatimingfunction) = %{version}
Provides:       crate(%{pkgname}/cavaluefunction) = %{version}

%description -n %{name}+camediatimingfunction
This metapackage enables feature "CAMediaTimingFunction" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CAValueFunction" feature.

%package     -n %{name}+cametaldisplaylink
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "CAMetalDisplayLink"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsobjcruntime) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsrunloop) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-metal-0.2/mtldrawable) >= 0.2.2
Provides:       crate(%{pkgname}/cametaldisplaylink) = %{version}

%description -n %{name}+cametaldisplaylink
This metapackage enables feature "CAMetalDisplayLink" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cametallayer
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "CAMetalLayer"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-metal-0.2/mtldevice) >= 0.2.2
Requires:       crate(objc2-metal-0.2/mtldrawable) >= 0.2.2
Requires:       crate(objc2-metal-0.2/mtlpixelformat) >= 0.2.2
Requires:       crate(objc2-metal-0.2/mtlresource) >= 0.2.2
Requires:       crate(objc2-metal-0.2/mtltexture) >= 0.2.2
Provides:       crate(%{pkgname}/cametallayer) = %{version}

%description -n %{name}+cametallayer
This metapackage enables feature "CAMetalLayer" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+carenderer
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "CARenderer"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/carenderer) = %{version}

%description -n %{name}+carenderer
This metapackage enables feature "CARenderer" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+careplicatorlayer
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "CAReplicatorLayer" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Provides:       crate(%{pkgname}/careplicatorlayer) = %{version}
Provides:       crate(%{pkgname}/catiledlayer) = %{version}

%description -n %{name}+careplicatorlayer
This metapackage enables feature "CAReplicatorLayer" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CATiledLayer" feature.

%package     -n %{name}+cascrolllayer
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "CAScrollLayer" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/cascrolllayer) = %{version}
Provides:       crate(%{pkgname}/catextlayer) = %{version}

%description -n %{name}+cascrolllayer
This metapackage enables feature "CAScrollLayer" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "CATextLayer" feature.

%package     -n %{name}+catransform3d
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "CATransform3D"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsvalue) >= 0.2.2
Provides:       crate(%{pkgname}/catransform3d) = %{version}

%description -n %{name}+catransform3d
This metapackage enables feature "CATransform3D" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+catransformlayer
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "CATransformLayer"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Provides:       crate(%{pkgname}/catransformlayer) = %{version}

%description -n %{name}+catransformlayer
This metapackage enables feature "CATransformLayer" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+all
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "all"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(%{pkgname}/block2) = %{version}
Requires:       crate(%{pkgname}/caanimation) = %{version}
Requires:       crate(%{pkgname}/cabase) = %{version}
Requires:       crate(%{pkgname}/caconstraintlayoutmanager) = %{version}
Requires:       crate(%{pkgname}/cadisplaylink) = %{version}
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
Requires:       crate(%{pkgname}/coreimage) = %{version}
Requires:       crate(%{pkgname}/corevideo) = %{version}
Requires:       crate(%{pkgname}/objc2-metal) = %{version}
Provides:       crate(%{pkgname}/all) = %{version}

%description -n %{name}+all
This metapackage enables feature "all" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+alloc
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block2-0.5/alloc) >= 0.5.1
Requires:       crate(objc2-0.5/alloc) >= 0.5.2
Requires:       crate(objc2-foundation-0.2/alloc) >= 0.2.2
Requires:       crate(objc2-metal-0.2/alloc) >= 0.2.2
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bitflags
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "bitflags"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bitflags-2) >= 2.5.0
Requires:       crate(objc2-foundation-0.2/bitflags) >= 0.2.2
Requires:       crate(objc2-metal-0.2/bitflags) >= 0.2.2
Provides:       crate(%{pkgname}/bitflags) = %{version}

%description -n %{name}+bitflags
This metapackage enables feature "bitflags" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+block2
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "block2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block2-0.5) >= 0.5.1
Requires:       crate(objc2-foundation-0.2/block2) >= 0.2.2
Requires:       crate(objc2-metal-0.2/block2) >= 0.2.2
Provides:       crate(%{pkgname}/block2) = %{version}

%description -n %{name}+block2
This metapackage enables feature "block2" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-metal
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "objc2-metal"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-metal-0.2) >= 0.2.2
Provides:       crate(%{pkgname}/objc2-metal) = %{version}

%description -n %{name}+objc2-metal
This metapackage enables feature "objc2-metal" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Bindings to the QuartzCore/CoreAnimation framework - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(bitflags-2/std) >= 2.5.0
Requires:       crate(block2-0.5/std) >= 0.5.1
Requires:       crate(objc2-0.5/std) >= 0.5.2
Requires:       crate(objc2-foundation-0.2/std) >= 0.2.2
Requires:       crate(objc2-metal-0.2/std) >= 0.2.2
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust objc2-quartz-core crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
