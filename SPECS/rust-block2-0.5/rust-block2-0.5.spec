# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name block2
%global full_version 0.5.1
%global pkgname block2-0.5

Name:           rust-block2-0.5
Version:        0.5.1
Release:        %autorelease
Summary:        Rust crate "block2"
License:        MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:2c132eebf10f5cad5289222520a4a058514204aed6d791f1cf4fe8088b82d15f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(objc2-0.5) >= 0.5.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/apple) = %{version}
Provides:       crate(%{pkgname}/unstable-objfw) = %{version}
Provides:       crate(%{pkgname}/unstable-private) = %{version}

%description
Source code for takopackized Rust crate "block2"

%package     -n %{name}+alloc
Summary:        Apple's C language extension of blocks - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-0.5/alloc) >= 0.5.2
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust block2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+compiler-rt
Summary:        Apple's C language extension of blocks - feature "compiler-rt"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-0.5/unstable-compiler-rt) >= 0.5.2
Provides:       crate(%{pkgname}/compiler-rt) = %{version}

%description -n %{name}+compiler-rt
This metapackage enables feature "compiler-rt" for the Rust block2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnustep-1-7
Summary:        Apple's C language extension of blocks - feature "gnustep-1-7"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-0.5/gnustep-1-7) >= 0.5.2
Provides:       crate(%{pkgname}/gnustep-1-7) = %{version}

%description -n %{name}+gnustep-1-7
This metapackage enables feature "gnustep-1-7" for the Rust block2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnustep-1-8
Summary:        Apple's C language extension of blocks - feature "gnustep-1-8" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gnustep-1-7) = %{version}
Requires:       crate(objc2-0.5/gnustep-1-8) >= 0.5.2
Provides:       crate(%{pkgname}/gnustep-1-8) = %{version}
Provides:       crate(%{pkgname}/unstable-winobjc) = %{version}

%description -n %{name}+gnustep-1-8
This metapackage enables feature "gnustep-1-8" for the Rust block2 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "unstable-winobjc" feature.

%package     -n %{name}+gnustep-1-9
Summary:        Apple's C language extension of blocks - feature "gnustep-1-9"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gnustep-1-8) = %{version}
Requires:       crate(objc2-0.5/gnustep-1-9) >= 0.5.2
Provides:       crate(%{pkgname}/gnustep-1-9) = %{version}

%description -n %{name}+gnustep-1-9
This metapackage enables feature "gnustep-1-9" for the Rust block2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnustep-2-0
Summary:        Apple's C language extension of blocks - feature "gnustep-2-0"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gnustep-1-9) = %{version}
Requires:       crate(objc2-0.5/gnustep-2-0) >= 0.5.2
Provides:       crate(%{pkgname}/gnustep-2-0) = %{version}

%description -n %{name}+gnustep-2-0
This metapackage enables feature "gnustep-2-0" for the Rust block2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnustep-2-1
Summary:        Apple's C language extension of blocks - feature "gnustep-2-1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gnustep-2-0) = %{version}
Requires:       crate(objc2-0.5/gnustep-2-1) >= 0.5.2
Provides:       crate(%{pkgname}/gnustep-2-1) = %{version}

%description -n %{name}+gnustep-2-1
This metapackage enables feature "gnustep-2-1" for the Rust block2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Apple's C language extension of blocks - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(objc2-0.5/std) >= 0.5.2
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust block2 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
