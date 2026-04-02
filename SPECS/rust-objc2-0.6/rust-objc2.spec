# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name objc2
%global full_version 0.6.4
%global pkgname objc2-0.6

Name:           rust-objc2-0.6
Version:        0.6.4
Release:        %autorelease
Summary:        Rust crate "objc2"
License:        MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:3a12a8ed07aefc768292f076dc3ac8c48f3781c8f2d5851dd3d98950e8c5a89f
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(objc2-encode-4.0) >= 4.1.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/disable-encoding-assertions)
Provides:       crate(%{pkgname}/objc2-proc-macros)
Provides:       crate(%{pkgname}/relax-sign-encoding)
Provides:       crate(%{pkgname}/relax-void-encoding)
Provides:       crate(%{pkgname}/unstable-apple-new)
Provides:       crate(%{pkgname}/unstable-arbitrary-self-types)
Provides:       crate(%{pkgname}/unstable-autoreleasesafe)
Provides:       crate(%{pkgname}/unstable-coerce-pointee)
Provides:       crate(%{pkgname}/unstable-darwin-objc)
Provides:       crate(%{pkgname}/unstable-objfw)
Provides:       crate(%{pkgname}/unstable-requires-macos)
Provides:       crate(%{pkgname}/verify)

%description
Source code for takopackized Rust crate "objc2"

%package     -n %{name}+alloc
Summary:        Objective-C interface and runtime bindings - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-encode-4.0/alloc) >= 4.1.0
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust objc2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+exception
Summary:        Objective-C interface and runtime bindings - feature "exception" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-exception-helper-0.1) >= 0.1.1
Provides:       crate(%{pkgname}/catch-all)
Provides:       crate(%{pkgname}/exception)

%description -n %{name}+exception
This metapackage enables feature "exception" for the Rust objc2 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "catch-all" feature.

%package     -n %{name}+gnustep-1-7
Summary:        Objective-C interface and runtime bindings - feature "gnustep-1-7" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/unstable-static-class)
Requires:       crate(objc2-exception-helper-0.1/gnustep-1-7) >= 0.1.1
Provides:       crate(%{pkgname}/gnustep-1-7)
Provides:       crate(%{pkgname}/unstable-compiler-rt)
Provides:       crate(%{pkgname}/unstable-gnustep-strict-apple-compat)

%description -n %{name}+gnustep-1-7
This metapackage enables feature "gnustep-1-7" for the Rust objc2 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "unstable-compiler-rt", and "unstable-gnustep-strict-apple-compat" features.

%package     -n %{name}+gnustep-1-8
Summary:        Objective-C interface and runtime bindings - feature "gnustep-1-8" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/gnustep-1-7)
Requires:       crate(objc2-exception-helper-0.1/gnustep-1-8) >= 0.1.1
Provides:       crate(%{pkgname}/gnustep-1-8)
Provides:       crate(%{pkgname}/unstable-winobjc)

%description -n %{name}+gnustep-1-8
This metapackage enables feature "gnustep-1-8" for the Rust objc2 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "unstable-winobjc" feature.

%package     -n %{name}+gnustep-1-9
Summary:        Objective-C interface and runtime bindings - feature "gnustep-1-9"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/gnustep-1-8)
Requires:       crate(objc2-exception-helper-0.1/gnustep-1-9) >= 0.1.1
Provides:       crate(%{pkgname}/gnustep-1-9)

%description -n %{name}+gnustep-1-9
This metapackage enables feature "gnustep-1-9" for the Rust objc2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnustep-2-0
Summary:        Objective-C interface and runtime bindings - feature "gnustep-2-0"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/gnustep-1-9)
Requires:       crate(objc2-exception-helper-0.1/gnustep-2-0) >= 0.1.1
Provides:       crate(%{pkgname}/gnustep-2-0)

%description -n %{name}+gnustep-2-0
This metapackage enables feature "gnustep-2-0" for the Rust objc2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnustep-2-1
Summary:        Objective-C interface and runtime bindings - feature "gnustep-2-1"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/gnustep-2-0)
Requires:       crate(objc2-exception-helper-0.1/gnustep-2-1) >= 0.1.1
Provides:       crate(%{pkgname}/gnustep-2-1)

%description -n %{name}+gnustep-2-1
This metapackage enables feature "gnustep-2-1" for the Rust objc2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Objective-C interface and runtime bindings - feature "std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(objc2-encode-4.0/std) >= 4.1.0
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust objc2 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+unstable-static-class
Summary:        Objective-C interface and runtime bindings - feature "unstable-static-class" and 3 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-proc-macros-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/unstable-static-class)
Provides:       crate(%{pkgname}/unstable-static-class-inlined)
Provides:       crate(%{pkgname}/unstable-static-sel)
Provides:       crate(%{pkgname}/unstable-static-sel-inlined)

%description -n %{name}+unstable-static-class
This metapackage enables feature "unstable-static-class" for the Rust objc2 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "unstable-static-class-inlined", "unstable-static-sel", and "unstable-static-sel-inlined" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
