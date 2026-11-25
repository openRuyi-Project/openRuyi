# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bincode-next
%global full_version 3.1.1
%global pkgname bincode-next-3

Name:           rust-bincode-next-3
Version:        3.1.1
Release:        %autorelease
Summary:        Rust crate "bincode-next"
License:        MIT or Apache-2.0
URL:            https://github.com/Apich-Organization/bincode
#!RemoteAsset:  sha256:1d6626829353ae29293be5c86f42de5f0468bc758af074b0c7d08f07e538ccbc
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(pastey-0.2/default) >= 0.2.0
Requires:       crate(rapidhash-4) >= 4.4.0
Requires:       crate(unty-next-0.1/default) >= 0.1.2

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/hw-acceleration) = %{version}
Provides:       crate(%{pkgname}/simd) = %{version}

%description
Source code for takopackized Rust crate "bincode-next"

%package     -n %{name}+alloc
Summary:        Compact, ultra-fast binary serialization format for Rust, optimized for networking and storage! - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/alloc) >= 1.0.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust bincode-next crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-fiber
Summary:        Compact, ultra-fast binary serialization format for Rust, optimized for networking and storage! - feature "async-fiber"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(futures-io-0.3/default) >= 0.3.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/async-fiber) = %{version}

%description -n %{name}+async-fiber
This metapackage enables feature "async-fiber" for the Rust bincode-next crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Compact, ultra-fast binary serialization format for Rust, optimized for networking and storage! - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/derive) = %{version}
Requires:       crate(%{pkgname}/simd) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust bincode-next crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+derive
Summary:        Compact, ultra-fast binary serialization format for Rust, optimized for networking and storage! - feature "derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bincode-derive-next-3/default) >= 3.1.1
Provides:       crate(%{pkgname}/derive) = %{version}

%description -n %{name}+derive
This metapackage enables feature "derive" for the Rust bincode-next crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+full
Summary:        Compact, ultra-fast binary serialization format for Rust, optimized for networking and storage! - feature "full"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/async-fiber) = %{version}
Requires:       crate(%{pkgname}/default) = %{version}
Requires:       crate(%{pkgname}/derive) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/simd) = %{version}
Requires:       crate(%{pkgname}/static-size) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/tokio) = %{version}
Requires:       crate(%{pkgname}/zero-copy) = %{version}
Provides:       crate(%{pkgname}/full) = %{version}

%description -n %{name}+full
This metapackage enables feature "full" for the Rust bincode-next crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fuzzing
Summary:        Compact, ultra-fast binary serialization format for Rust, optimized for networking and storage! - feature "fuzzing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/zero-copy) = %{version}
Requires:       crate(arbitrary-1/default) >= 1.3.0
Provides:       crate(%{pkgname}/fuzzing) = %{version}

%description -n %{name}+fuzzing
This metapackage enables feature "fuzzing" for the Rust bincode-next crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Compact, ultra-fast binary serialization format for Rust, optimized for networking and storage! - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust bincode-next crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+static-size
Summary:        Compact, ultra-fast binary serialization format for Rust, optimized for networking and storage! - feature "static-size"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bincode-derive-next-3/static-size) >= 3.1.1
Provides:       crate(%{pkgname}/static-size) = %{version}

%description -n %{name}+static-size
This metapackage enables feature "static-size" for the Rust bincode-next crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Compact, ultra-fast binary serialization format for Rust, optimized for networking and storage! - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(serde-1/std) >= 1.0.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust bincode-next crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Compact, ultra-fast binary serialization format for Rust, optimized for networking and storage! - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async-fiber) = %{version}
Requires:       crate(tokio-1) >= 1.50.0
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust bincode-next crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zero-copy
Summary:        Compact, ultra-fast binary serialization format for Rust, optimized for networking and storage! - feature "zero-copy"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bincode-derive-next-3/zero-copy) >= 3.1.1
Provides:       crate(%{pkgname}/zero-copy) = %{version}

%description -n %{name}+zero-copy
This metapackage enables feature "zero-copy" for the Rust bincode-next crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
