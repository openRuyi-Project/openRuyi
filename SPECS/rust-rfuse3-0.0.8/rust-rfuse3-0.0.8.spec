# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rfuse3
%global full_version 0.0.8
%global pkgname rfuse3-0.0.8

Name:           rust-rfuse3-0.0.8
Version:        0.0.8
Release:        %autorelease
Summary:        Rust crate "rfuse3"
License:        MIT
URL:            https://github.com/r2cn-dev/rk8s/tree/main/project/rfuse3
#!RemoteAsset:  sha256:c5d7bea55817b58bd3a706ac0671f9aedc06d2d91e2f68272bd4fbe62f817d2b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(aligned-box-0.3/default) >= 0.3.0
Requires:       crate(async-notify-0.3/default) >= 0.3.0
Requires:       crate(async-trait-0.1/default) >= 0.1.89
Requires:       crate(bincode-1/default) >= 1.3.3
Requires:       crate(bytes-1/default) >= 1.10.1
Requires:       crate(dashmap-6/default) >= 6.1.0
Requires:       crate(futures-channel-0.3/default) >= 0.3.31
Requires:       crate(futures-channel-0.3/sink) >= 0.3.31
Requires:       crate(futures-util-0.3/default) >= 0.3.31
Requires:       crate(futures-util-0.3/sink) >= 0.3.31
Requires:       crate(libc-0.2/default) >= 0.2.175
Requires:       crate(nix-0.29/default) >= 0.29.0
Requires:       crate(nix-0.29/dir) >= 0.29.0
Requires:       crate(nix-0.29/fs) >= 0.29.0
Requires:       crate(nix-0.29/hostname) >= 0.29.0
Requires:       crate(nix-0.29/mman) >= 0.29.0
Requires:       crate(nix-0.29/mount) >= 0.29.0
Requires:       crate(nix-0.29/process) >= 0.29.0
Requires:       crate(nix-0.29/resource) >= 0.29.0
Requires:       crate(nix-0.29/sched) >= 0.29.0
Requires:       crate(nix-0.29/signal) >= 0.29.0
Requires:       crate(nix-0.29/socket) >= 0.29.0
Requires:       crate(nix-0.29/term) >= 0.29.0
Requires:       crate(nix-0.29/user) >= 0.29.0
Requires:       crate(serde-1/default) >= 1.0.228
Requires:       crate(serde-1/derive) >= 1.0.228
Requires:       crate(slab-0.4/default) >= 0.4.9
Requires:       crate(tracing-0.1/attributes) >= 0.1.41
Requires:       crate(tracing-0.1/default) >= 0.1.41
Requires:       crate(trait-make-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/buffer-pool) = %{version}
Provides:       crate(%{pkgname}/file-lock) = %{version}

%description
Source code for takopackized Rust crate "rfuse3"

%package     -n %{name}+async-io-runtime
Summary:        FUSE user-space library async version implementation - feature "async-io-runtime"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-fs-2/default) >= 2.1.1
Requires:       crate(async-global-executor-2/default) >= 2.4.1
Requires:       crate(async-io-2/default) >= 2.3.1
Requires:       crate(async-lock-3/default) >= 3.3.0
Requires:       crate(async-process-2/default) >= 2.1.0
Requires:       crate(futures-util-0.3/io) >= 0.3.31
Requires:       crate(futures-util-0.3/sink) >= 0.3.31
Provides:       crate(%{pkgname}/async-io-runtime) = %{version}

%description -n %{name}+async-io-runtime
This metapackage enables feature "async-io-runtime" for the Rust rfuse3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        FUSE user-space library async version implementation - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tokio-runtime) = %{version}
Requires:       crate(%{pkgname}/unprivileged) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust rfuse3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-runtime
Summary:        FUSE user-space library async version implementation - feature "tokio-runtime"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/default) >= 1.48.0
Requires:       crate(tokio-1/full) >= 1.48.0
Provides:       crate(%{pkgname}/tokio-runtime) = %{version}

%description -n %{name}+tokio-runtime
This metapackage enables feature "tokio-runtime" for the Rust rfuse3 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unprivileged
Summary:        FUSE user-space library async version implementation - feature "unprivileged"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(nix-0.29/dir) >= 0.29.0
Requires:       crate(nix-0.29/fs) >= 0.29.0
Requires:       crate(nix-0.29/hostname) >= 0.29.0
Requires:       crate(nix-0.29/mman) >= 0.29.0
Requires:       crate(nix-0.29/mount) >= 0.29.0
Requires:       crate(nix-0.29/process) >= 0.29.0
Requires:       crate(nix-0.29/resource) >= 0.29.0
Requires:       crate(nix-0.29/sched) >= 0.29.0
Requires:       crate(nix-0.29/signal) >= 0.29.0
Requires:       crate(nix-0.29/socket) >= 0.29.0
Requires:       crate(nix-0.29/term) >= 0.29.0
Requires:       crate(nix-0.29/user) >= 0.29.0
Requires:       crate(which-4/default) >= 4.4.2
Provides:       crate(%{pkgname}/unprivileged) = %{version}

%description -n %{name}+unprivileged
This metapackage enables feature "unprivileged" for the Rust rfuse3 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
