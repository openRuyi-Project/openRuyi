# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name futures-executor-preview
%global full_version 0.3.0-alpha.15
%global pkgname futures-executor-preview-0.3.0-alpha.15

Name:           rust-futures-executor-preview-0.3.0-alpha.15
Version:        0.3.0
Release:        %autorelease
Summary:        Rust crate "futures-executor-preview"
License:        MIT OR Apache-2.0
URL:            https://rust-lang-nursery.github.io/futures-rs
#!RemoteAsset:  sha256:0a75c64f20734619b4668e87f902544ce8c108dfcb6c9b6b2fcefdd1a848c15a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(futures-channel-preview-0.3.0-alpha.15) >= 0.3.0-alpha.15
Requires:       crate(futures-core-preview-0.3.0-alpha.15) >= 0.3.0-alpha.15
Requires:       crate(futures-util-preview-0.3.0-alpha.15) >= 0.3.0-alpha.15
Requires:       crate(pin-utils-0.1.0-alpha.4/default) >= 0.1.0-alpha.4

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "futures-executor-preview"

%package     -n %{name}+num-cpus
Summary:        Executors for asynchronous tasks based on the futures-rs library - feature "num_cpus"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-cpus-1/default) >= 1.8.0
Provides:       crate(%{pkgname}/num-cpus) = %{version}

%description -n %{name}+num-cpus
This metapackage enables feature "num_cpus" for the Rust futures-executor-preview crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Executors for asynchronous tasks based on the futures-rs library - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/num-cpus) = %{version}
Requires:       crate(futures-channel-preview-0.3.0-alpha.15/std) >= 0.3.0-alpha.15
Requires:       crate(futures-core-preview-0.3.0-alpha.15/std) >= 0.3.0-alpha.15
Requires:       crate(futures-util-preview-0.3.0-alpha.15/std) >= 0.3.0-alpha.15
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust futures-executor-preview crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%install -a
# Keep prerelease sources separate from the corresponding stable release.
mv %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version} %{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
