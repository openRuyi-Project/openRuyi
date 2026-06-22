# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pprof
%global full_version 0.14.1
%global pkgname pprof-0.14

Name:           rust-pprof-0.14
Version:        0.14.1
Release:        %autorelease
Summary:        Rust crate "pprof"
License:        Apache-2.0
URL:            https://github.com/tikv/pprof-rs
#!RemoteAsset:  sha256:afad4d4df7b31280028245f152d5a575083e2abb822d05736f5e47653e77689f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(aligned-vec-0.6/default) >= 0.6.0
Requires:       crate(backtrace-0.3/default) >= 0.3.0
Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(findshlibs-0.10/default) >= 0.10.0
Requires:       crate(libc-0.2/default) >= 0.2.66
Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(nix-0.26/fs) >= 0.26.0
Requires:       crate(nix-0.26/signal) >= 0.26.0
Requires:       crate(once-cell-1/default) >= 1.9.0
Requires:       crate(smallvec-1/default) >= 1.7.0
Requires:       crate(spin-0.10/default) >= 0.10.0
Requires:       crate(symbolic-demangle-12/rust) >= 12.1.0
Requires:       crate(tempfile-3/default) >= 3.1.0
Requires:       crate(thiserror-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/frame-pointer) = %{version}
# Fix it. Main package should not provides feature which subpackage provides.
# Provides:       crate(%{pkgname}/protobuf) = %{version}

%description
Source code for takopackized Rust crate "pprof"

%package     -n %{name}+cpp
Summary:        Internal perf tools for rust programs - feature "cpp" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(symbolic-demangle-12/cpp) >= 12.1.0
Requires:       crate(symbolic-demangle-12/rust) >= 12.1.0
Provides:       crate(%{pkgname}/cpp) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+cpp
This metapackage enables feature "cpp" for the Rust pprof crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+criterion
Summary:        Internal perf tools for rust programs - feature "criterion"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(criterion-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/criterion) = %{version}

%description -n %{name}+criterion
This metapackage enables feature "criterion" for the Rust pprof crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+inferno
Summary:        Internal perf tools for rust programs - feature "inferno" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(inferno-0.11/nameattr) >= 0.11.0
Provides:       crate(%{pkgname}/flamegraph) = %{version}
Provides:       crate(%{pkgname}/inferno) = %{version}

%description -n %{name}+inferno
This metapackage enables feature "inferno" for the Rust pprof crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "flamegraph" feature.

%package     -n %{name}+prost
Summary:        Internal perf tools for rust programs - feature "prost"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(prost-0.12/default) >= 0.12.0
Provides:       crate(%{pkgname}/prost) = %{version}

%description -n %{name}+prost
This metapackage enables feature "prost" for the Rust pprof crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+prost-build
Summary:        Internal perf tools for rust programs - feature "prost-build"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(prost-build-0.12/default) >= 0.12.0
Provides:       crate(%{pkgname}/prost-build) = %{version}

%description -n %{name}+prost-build
This metapackage enables feature "prost-build" for the Rust pprof crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+prost-codec
Summary:        Internal perf tools for rust programs - feature "prost-codec"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/prost) = %{version}
Requires:       crate(%{pkgname}/prost-build) = %{version}
Requires:       crate(%{pkgname}/prost-derive) = %{version}
Requires:       crate(%{pkgname}/protobuf) = %{version}
Requires:       crate(%{pkgname}/sha2) = %{version}
Provides:       crate(%{pkgname}/prost-codec) = %{version}

%description -n %{name}+prost-codec
This metapackage enables feature "prost-codec" for the Rust pprof crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+prost-derive
Summary:        Internal perf tools for rust programs - feature "prost-derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(prost-derive-0.12/default) >= 0.12.0
Provides:       crate(%{pkgname}/prost-derive) = %{version}

%description -n %{name}+prost-derive
This metapackage enables feature "prost-derive" for the Rust pprof crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+protobuf
Summary:        Internal perf tools for rust programs - feature "protobuf"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(protobuf-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/protobuf) = %{version}

%description -n %{name}+protobuf
This metapackage enables feature "protobuf" for the Rust pprof crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+protobuf-codec
Summary:        Internal perf tools for rust programs - feature "protobuf-codec"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/protobuf) = %{version}
Requires:       crate(%{pkgname}/protobuf-codegen-pure) = %{version}
Provides:       crate(%{pkgname}/protobuf-codec) = %{version}

%description -n %{name}+protobuf-codec
This metapackage enables feature "protobuf-codec" for the Rust pprof crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+protobuf-codegen-pure
Summary:        Internal perf tools for rust programs - feature "protobuf-codegen-pure"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(protobuf-codegen-pure-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/protobuf-codegen-pure) = %{version}

%description -n %{name}+protobuf-codegen-pure
This metapackage enables feature "protobuf-codegen-pure" for the Rust pprof crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha2
Summary:        Internal perf tools for rust programs - feature "sha2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sha2-0.10/default) >= 0.10.0
Provides:       crate(%{pkgname}/sha2) = %{version}

%description -n %{name}+sha2
This metapackage enables feature "sha2" for the Rust pprof crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
