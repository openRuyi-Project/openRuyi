# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name futures-util
%global full_version 0.3.32
%global pkgname futures-util-0.3

Name:           rust-futures-util-0.3
Version:        0.3.32
Release:        %autorelease
Summary:        Rust crate "futures-util"
License:        MIT OR Apache-2.0
URL:            https://rust-lang.github.io/futures-rs
#!RemoteAsset:  sha256:389ca41296e6190b48053de0321d02a77f32f8a5d2461dd38762c0593805c6d6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(futures-core-0.3) >= 0.3.32
Requires:       crate(futures-task-0.3) >= 0.3.32
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.6
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/async-await) = %{version}
Provides:       crate(%{pkgname}/bilock) = %{version}
Provides:       crate(%{pkgname}/cfg-target-has-atomic) = %{version}

%description
Source code for takopackized Rust crate "futures-util"

%package     -n %{name}+alloc
Summary:        Common utilities and extension traits for the futures-rs library - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/slab) = %{version}
Requires:       crate(futures-core-0.3/alloc) >= 0.3.32
Requires:       crate(futures-task-0.3/alloc) >= 0.3.32
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust futures-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-await-macro
Summary:        Common utilities and extension traits for the futures-rs library - feature "async-await-macro"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async-await) = %{version}
Requires:       crate(%{pkgname}/futures-macro) = %{version}
Provides:       crate(%{pkgname}/async-await-macro) = %{version}

%description -n %{name}+async-await-macro
This metapackage enables feature "async-await-macro" for the Rust futures-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+channel
Summary:        Common utilities and extension traits for the futures-rs library - feature "channel"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/futures-channel) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/channel) = %{version}

%description -n %{name}+channel
This metapackage enables feature "channel" for the Rust futures-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+compat
Summary:        Common utilities and extension traits for the futures-rs library - feature "compat"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/futures-01) = %{version}
Requires:       crate(%{pkgname}/libc) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/compat) = %{version}

%description -n %{name}+compat
This metapackage enables feature "compat" for the Rust futures-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Common utilities and extension traits for the futures-rs library - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async-await) = %{version}
Requires:       crate(%{pkgname}/async-await-macro) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust futures-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-channel
Summary:        Common utilities and extension traits for the futures-rs library - feature "futures-channel"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-channel-0.3/std) >= 0.3.32
Provides:       crate(%{pkgname}/futures-channel) = %{version}

%description -n %{name}+futures-channel
This metapackage enables feature "futures-channel" for the Rust futures-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-io
Summary:        Common utilities and extension traits for the futures-rs library - feature "futures-io"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-io-0.3/std) >= 0.3.32
Provides:       crate(%{pkgname}/futures-io) = %{version}

%description -n %{name}+futures-io
This metapackage enables feature "futures-io" for the Rust futures-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-macro
Summary:        Common utilities and extension traits for the futures-rs library - feature "futures-macro"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-macro-0.3) >= 0.3.32
Provides:       crate(%{pkgname}/futures-macro) = %{version}

%description -n %{name}+futures-macro
This metapackage enables feature "futures-macro" for the Rust futures-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-sink
Summary:        Common utilities and extension traits for the futures-rs library - feature "futures-sink" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-sink-0.3) >= 0.3.32
Provides:       crate(%{pkgname}/futures-sink) = %{version}
Provides:       crate(%{pkgname}/sink) = %{version}

%description -n %{name}+futures-sink
This metapackage enables feature "futures-sink" for the Rust futures-util crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "sink" feature.

%package     -n %{name}+futures-01
Summary:        Common utilities and extension traits for the futures-rs library - feature "futures_01"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-0.1/default) >= 0.1.25
Provides:       crate(%{pkgname}/futures-01) = %{version}

%description -n %{name}+futures-01
This metapackage enables feature "futures_01" for the Rust futures-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+io
Summary:        Common utilities and extension traits for the futures-rs library - feature "io" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/futures-io) = %{version}
Requires:       crate(%{pkgname}/memchr) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/io) = %{version}
Provides:       crate(%{pkgname}/write-all-vectored) = %{version}

%description -n %{name}+io
This metapackage enables feature "io" for the Rust futures-util crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "write-all-vectored" feature.

%package     -n %{name}+io-compat
Summary:        Common utilities and extension traits for the futures-rs library - feature "io-compat"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/compat) = %{version}
Requires:       crate(%{pkgname}/io) = %{version}
Requires:       crate(%{pkgname}/libc) = %{version}
Requires:       crate(%{pkgname}/tokio-io) = %{version}
Provides:       crate(%{pkgname}/io-compat) = %{version}

%description -n %{name}+io-compat
This metapackage enables feature "io-compat" for the Rust futures-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libc
Summary:        Common utilities and extension traits for the futures-rs library - feature "libc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2/default) >= 0.2.26
Provides:       crate(%{pkgname}/libc) = %{version}

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust futures-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+memchr
Summary:        Common utilities and extension traits for the futures-rs library - feature "memchr"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(memchr-2/default) >= 2.2.0
Provides:       crate(%{pkgname}/memchr) = %{version}

%description -n %{name}+memchr
This metapackage enables feature "memchr" for the Rust futures-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+portable-atomic
Summary:        Common utilities and extension traits for the futures-rs library - feature "portable-atomic"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-core-0.3/portable-atomic) >= 0.3.32
Provides:       crate(%{pkgname}/portable-atomic) = %{version}

%description -n %{name}+portable-atomic
This metapackage enables feature "portable-atomic" for the Rust futures-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+slab
Summary:        Common utilities and extension traits for the futures-rs library - feature "slab"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(slab-0.4) >= 0.4.7
Provides:       crate(%{pkgname}/slab) = %{version}

%description -n %{name}+slab
This metapackage enables feature "slab" for the Rust futures-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+spin
Summary:        Common utilities and extension traits for the futures-rs library - feature "spin"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(spin-0.10/default) >= 0.10.0
Provides:       crate(%{pkgname}/spin) = %{version}

%description -n %{name}+spin
This metapackage enables feature "spin" for the Rust futures-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Common utilities and extension traits for the futures-rs library - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(futures-core-0.3/std) >= 0.3.32
Requires:       crate(futures-task-0.3/std) >= 0.3.32
Requires:       crate(slab-0.4/std) >= 0.4.7
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust futures-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-io
Summary:        Common utilities and extension traits for the futures-rs library - feature "tokio-io"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-io-0.1/default) >= 0.1.9
Provides:       crate(%{pkgname}/tokio-io) = %{version}

%description -n %{name}+tokio-io
This metapackage enables feature "tokio-io" for the Rust futures-util crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable
Summary:        Common utilities and extension traits for the futures-rs library - feature "unstable"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-core-0.3/unstable) >= 0.3.32
Requires:       crate(futures-task-0.3/unstable) >= 0.3.32
Provides:       crate(%{pkgname}/unstable) = %{version}

%description -n %{name}+unstable
This metapackage enables feature "unstable" for the Rust futures-util crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
