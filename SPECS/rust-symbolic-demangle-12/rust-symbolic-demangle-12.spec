# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name symbolic-demangle
%global full_version 12.18.3
%global pkgname symbolic-demangle-12

Name:           rust-symbolic-demangle-12
Version:        12.18.3
Release:        %autorelease
Summary:        Rust crate "symbolic-demangle"
License:        MIT
URL:            https://github.com/getsentry/symbolic
#!RemoteAsset:  sha256:912017718eb4d21930546245af9a3475c9dccf15675a5c215664e76621afc471
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(symbolic-common-12/default) >= 12.18.3
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "symbolic-demangle"

%package     -n %{name}+cc
Summary:        Demangle symbols from various languages and compilers - feature "cc" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cc-1/default) >= 1.0.79
Provides:       crate(%{pkgname}/cc) = %{version}
Provides:       crate(%{pkgname}/swift) = %{version}

%description -n %{name}+cc
This metapackage enables feature "cc" for the Rust symbolic-demangle crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "swift" feature.

%package     -n %{name}+cpp-demangle
Summary:        Demangle symbols from various languages and compilers - feature "cpp_demangle" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cpp-demangle-0.4/default) >= 0.4.1
Provides:       crate(%{pkgname}/cpp) = %{version}
Provides:       crate(%{pkgname}/cpp-demangle) = %{version}

%description -n %{name}+cpp-demangle
This metapackage enables feature "cpp_demangle" for the Rust symbolic-demangle crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "cpp" feature.

%package     -n %{name}+default
Summary:        Demangle symbols from various languages and compilers - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/cpp) = %{version}
Requires:       crate(%{pkgname}/msvc) = %{version}
Requires:       crate(%{pkgname}/rust) = %{version}
Requires:       crate(%{pkgname}/swift) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust symbolic-demangle crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+msvc-demangler
Summary:        Demangle symbols from various languages and compilers - feature "msvc-demangler" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(msvc-demangler-0.11/default) >= 0.11.0
Provides:       crate(%{pkgname}/msvc) = %{version}
Provides:       crate(%{pkgname}/msvc-demangler) = %{version}

%description -n %{name}+msvc-demangler
This metapackage enables feature "msvc-demangler" for the Rust symbolic-demangle crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "msvc" feature.

%package     -n %{name}+rustc-demangle
Summary:        Demangle symbols from various languages and compilers - feature "rustc-demangle" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustc-demangle-0.1/default) >= 0.1.21
Provides:       crate(%{pkgname}/rust) = %{version}
Provides:       crate(%{pkgname}/rustc-demangle) = %{version}

%description -n %{name}+rustc-demangle
This metapackage enables feature "rustc-demangle" for the Rust symbolic-demangle crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "rust" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
