# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name block2
%global full_version 0.6.2
%global pkgname block2-0.6

Name:           rust-block2-0.6
Version:        0.6.2
Release:        %autorelease
Summary:        Rust crate "block2"
License:        MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:cdeb9d870516001442e364c5220d3574d2da8dc765554b4a617230d33fa58ef5
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(objc2-0.6/std) >= 0.6.4
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/unstable-coerce-pointee)
Provides:       crate(%{pkgname}/unstable-objfw)
Provides:       crate(%{pkgname}/unstable-private)

%description
Source code for takopackized Rust crate "block2"

%package     -n %{name}+compiler-rt
Summary:        Apple's C language extension of blocks - feature "compiler-rt"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-0.6/std) >= 0.6.4
Requires:       crate(objc2-0.6/unstable-compiler-rt) >= 0.6.4
Provides:       crate(%{pkgname}/compiler-rt)

%description -n %{name}+compiler-rt
This metapackage enables feature "compiler-rt" for the Rust block2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnustep-1-7
Summary:        Apple's C language extension of blocks - feature "gnustep-1-7"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-0.6/gnustep-1-7) >= 0.6.4
Requires:       crate(objc2-0.6/std) >= 0.6.4
Provides:       crate(%{pkgname}/gnustep-1-7)

%description -n %{name}+gnustep-1-7
This metapackage enables feature "gnustep-1-7" for the Rust block2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnustep-1-8
Summary:        Apple's C language extension of blocks - feature "gnustep-1-8" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/gnustep-1-7)
Requires:       crate(objc2-0.6/gnustep-1-8) >= 0.6.4
Requires:       crate(objc2-0.6/std) >= 0.6.4
Provides:       crate(%{pkgname}/gnustep-1-8)
Provides:       crate(%{pkgname}/unstable-winobjc)

%description -n %{name}+gnustep-1-8
This metapackage enables feature "gnustep-1-8" for the Rust block2 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "unstable-winobjc" feature.

%package     -n %{name}+gnustep-1-9
Summary:        Apple's C language extension of blocks - feature "gnustep-1-9"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/gnustep-1-8)
Requires:       crate(objc2-0.6/gnustep-1-9) >= 0.6.4
Requires:       crate(objc2-0.6/std) >= 0.6.4
Provides:       crate(%{pkgname}/gnustep-1-9)

%description -n %{name}+gnustep-1-9
This metapackage enables feature "gnustep-1-9" for the Rust block2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnustep-2-0
Summary:        Apple's C language extension of blocks - feature "gnustep-2-0"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/gnustep-1-9)
Requires:       crate(objc2-0.6/gnustep-2-0) >= 0.6.4
Requires:       crate(objc2-0.6/std) >= 0.6.4
Provides:       crate(%{pkgname}/gnustep-2-0)

%description -n %{name}+gnustep-2-0
This metapackage enables feature "gnustep-2-0" for the Rust block2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnustep-2-1
Summary:        Apple's C language extension of blocks - feature "gnustep-2-1"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/gnustep-2-0)
Requires:       crate(objc2-0.6/gnustep-2-1) >= 0.6.4
Requires:       crate(objc2-0.6/std) >= 0.6.4
Provides:       crate(%{pkgname}/gnustep-2-1)

%description -n %{name}+gnustep-2-1
This metapackage enables feature "gnustep-2-1" for the Rust block2 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
