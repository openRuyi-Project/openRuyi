# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name objc2
%global full_version 0.5.2
%global pkgname objc2-0.5

Name:           rust-objc2-0.5
Version:        0.5.2
Release:        %autorelease
Summary:        Rust crate "objc2"
License:        MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:46a785d4eeff09c14c487497c162e92766fbb3e4059a71840cecc03d9a50b804
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(objc-sys-0.3) >= 0.3.5
Requires:       crate(objc2-encode-4) >= 4.0.3
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/apple) = %{version}
Provides:       crate(%{pkgname}/relax-sign-encoding) = %{version}
Provides:       crate(%{pkgname}/relax-void-encoding) = %{version}
Provides:       crate(%{pkgname}/unstable-apple-new) = %{version}
Provides:       crate(%{pkgname}/unstable-autoreleasesafe) = %{version}
Provides:       crate(%{pkgname}/unstable-c-unwind) = %{version}
Provides:       crate(%{pkgname}/unstable-msg-send-always-comma) = %{version}
Provides:       crate(%{pkgname}/verify) = %{version}

%description
Source code for takopackized Rust crate "objc2"

%package     -n %{name}+alloc
Summary:        Objective-C interface and runtime bindings - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc-sys-0.3/alloc) >= 0.3.5
Requires:       crate(objc2-encode-4/alloc) >= 4.0.3
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust objc2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+exception
Summary:        Objective-C interface and runtime bindings - feature "exception" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc-sys-0.3/unstable-exception) >= 0.3.5
Provides:       crate(%{pkgname}/catch-all) = %{version}
Provides:       crate(%{pkgname}/exception) = %{version}

%description -n %{name}+exception
This metapackage enables feature "exception" for the Rust objc2 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "catch-all" feature.

%package     -n %{name}+gnustep-1-7
Summary:        Objective-C interface and runtime bindings - feature "gnustep-1-7" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/unstable-static-class) = %{version}
Requires:       crate(objc-sys-0.3/gnustep-1-7) >= 0.3.5
Provides:       crate(%{pkgname}/gnustep-1-7) = %{version}
Provides:       crate(%{pkgname}/unstable-compiler-rt) = %{version}

%description -n %{name}+gnustep-1-7
This metapackage enables feature "gnustep-1-7" for the Rust objc2 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "unstable-compiler-rt" feature.

%package     -n %{name}+gnustep-1-8
Summary:        Objective-C interface and runtime bindings - feature "gnustep-1-8"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gnustep-1-7) = %{version}
Requires:       crate(objc-sys-0.3/gnustep-1-8) >= 0.3.5
Provides:       crate(%{pkgname}/gnustep-1-8) = %{version}

%description -n %{name}+gnustep-1-8
This metapackage enables feature "gnustep-1-8" for the Rust objc2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnustep-1-9
Summary:        Objective-C interface and runtime bindings - feature "gnustep-1-9"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gnustep-1-8) = %{version}
Requires:       crate(objc-sys-0.3/gnustep-1-9) >= 0.3.5
Provides:       crate(%{pkgname}/gnustep-1-9) = %{version}

%description -n %{name}+gnustep-1-9
This metapackage enables feature "gnustep-1-9" for the Rust objc2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnustep-2-0
Summary:        Objective-C interface and runtime bindings - feature "gnustep-2-0"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gnustep-1-9) = %{version}
Requires:       crate(objc-sys-0.3/gnustep-2-0) >= 0.3.5
Provides:       crate(%{pkgname}/gnustep-2-0) = %{version}

%description -n %{name}+gnustep-2-0
This metapackage enables feature "gnustep-2-0" for the Rust objc2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnustep-2-1
Summary:        Objective-C interface and runtime bindings - feature "gnustep-2-1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gnustep-2-0) = %{version}
Requires:       crate(objc-sys-0.3/gnustep-2-1) >= 0.3.5
Provides:       crate(%{pkgname}/gnustep-2-1) = %{version}

%description -n %{name}+gnustep-2-1
This metapackage enables feature "gnustep-2-1" for the Rust objc2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+malloc-buf
Summary:        Objective-C interface and runtime bindings - feature "malloc_buf" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(malloc-buf-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/malloc) = %{version}
Provides:       crate(%{pkgname}/malloc-buf) = %{version}

%description -n %{name}+malloc-buf
This metapackage enables feature "malloc_buf" for the Rust objc2 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "malloc" feature.

%package     -n %{name}+objc2-proc-macros
Summary:        Objective-C interface and runtime bindings - feature "objc2-proc-macros" and 4 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-proc-macros-0.1/default) >= 0.1.3
Provides:       crate(%{pkgname}/objc2-proc-macros) = %{version}
Provides:       crate(%{pkgname}/unstable-static-class) = %{version}
Provides:       crate(%{pkgname}/unstable-static-class-inlined) = %{version}
Provides:       crate(%{pkgname}/unstable-static-sel) = %{version}
Provides:       crate(%{pkgname}/unstable-static-sel-inlined) = %{version}

%description -n %{name}+objc2-proc-macros
This metapackage enables feature "objc2-proc-macros" for the Rust objc2 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "unstable-static-class", "unstable-static-class-inlined", "unstable-static-sel", and "unstable-static-sel-inlined" features.

%package     -n %{name}+std
Summary:        Objective-C interface and runtime bindings - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(objc-sys-0.3/std) >= 0.3.5
Requires:       crate(objc2-encode-4/std) >= 4.0.3
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust objc2 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
