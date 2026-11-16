# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: A.Donz <avrova.minix@donz.si>
# SPDX-FileContributor: MMLA-org <https://github.com/MMLA-org>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Sponsored by cha86.dev <https://cha86.dev>

%global srcname py-spy
%global pypi_name py_spy
%ifarch riscv64
%global llvm_maj_ver 22
%global toolchain clang
%endif

Name:           python-%{srcname}
Version:        0.4.1
Release:        %autorelease
Summary:        Sampling profiler for Python programs
License:        MIT
URL:            https://github.com/benfred/py-spy
VCS:            git:https://github.com/benfred/py-spy.git
#!RemoteAsset:  sha256:e53aa53daa2e47c2eef97dd2455b47bb3a7e7f962796a86cc3e7dbde8e6f4db4
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name} -L

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(maturin)
BuildRequires:  python3dist(pip)
BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  pkgconfig(libunwind)
BuildRequires:  crate(anyhow-1/default) >= 1.0.0
BuildRequires:  crate(clap-3/default) >= 3.2.0
BuildRequires:  crate(clap-complete-3/default) >= 3.2.0
BuildRequires:  crate(console-0.16/default) >= 0.16.0
BuildRequires:  crate(ctrlc-3/default) >= 3.0.0
BuildRequires:  crate(indicatif-0.18/default) >= 0.18.0
BuildRequires:  crate(env-logger-0.11/default) >= 0.11.0
BuildRequires:  crate(goblin-0.10/default) >= 0.10.0
BuildRequires:  crate(inferno-0.12/default) >= 0.12.3
BuildRequires:  crate(lazy-static-1/default) >= 1.4.0
BuildRequires:  crate(libc-0.2/default) >= 0.2.0
BuildRequires:  crate(log-0.4/default) >= 0.4.0
BuildRequires:  crate(lru-0.10/default) >= 0.10.0
BuildRequires:  crate(num-traits-0.2/default) >= 0.2.0
BuildRequires:  crate(regex-1/default) >= 1.6.0
BuildRequires:  crate(tempfile-3/default) >= 3.6.0
BuildRequires:  crate(page-size-0.6/default) >= 0.6.0
BuildRequires:  crate(proc-maps-0.4/default) >= 0.4.0
BuildRequires:  crate(memmap2-0.9/default) >= 0.9.4
BuildRequires:  crate(cpp-demangle-0.4/default) >= 0.4.0
BuildRequires:  crate(serde-1/default) >= 1.0.0
BuildRequires:  crate(serde-1/derive) >= 1.0.0
BuildRequires:  crate(serde-json-1/default) >= 1.0.0
BuildRequires:  crate(rand-0.8/default) >= 0.8.0
BuildRequires:  crate(rand-distr-0.4/default) >= 0.4.0
BuildRequires:  crate(remoteprocess-0.5/default) >= 0.5.1
BuildRequires:  crate(chrono-0.4/default) >= 0.4.26
BuildRequires:  crate(termios-0.3/default) >= 0.3.3
%ifarch riscv64
BuildRequires:  clang
BuildRequires:  clang(major) = %{llvm_maj_ver}
BuildRequires:  compiler-rt(major) = %{llvm_maj_ver}
BuildRequires:  lld(major) = %{llvm_maj_ver}
BuildRequires:  llvm(major) = %{llvm_maj_ver}
%endif

Provides:       python3dist(py-spy) = %{version}-%{release}

%description
py-spy is a sampling profiler for Python programs. It reads the state of a
running Python process without requiring changes to the profiled program.

%prep -a
%rust_setup_registry
rm -f Cargo.lock
# The test-data dev-dependency is not packaged, and cargo metadata resolves
# dev-dependencies even for release builds.  Drop the entries so the offline
# system-registry resolution succeeds.
sed -i -e '/^\[dev-dependencies\]/d' -e '/^py-spy-testdata = /d' Cargo.toml

%generate_buildrequires
export CARGO_NET_OFFLINE=true
%pyproject_buildrequires

%build -p
export CARGO_NET_OFFLINE=true
%ifarch riscv64
export CC="${CC:-clang}"
export CXX="${CXX:-clang++}"
export CARGO_TARGET_RISCV64GC_UNKNOWN_LINUX_GNU_LINKER="${CARGO_TARGET_RISCV64GC_UNKNOWN_LINUX_GNU_LINKER:-clang}"
export CARGO_TARGET_RISCV64GC_UNKNOWN_LINUX_GNU_RUSTFLAGS="${CARGO_TARGET_RISCV64GC_UNKNOWN_LINUX_GNU_RUSTFLAGS:-} -C link-arg=-fuse-ld=lld"
%endif

%install -p
install -Dpm 0755 target/release/py-spy %{buildroot}%{_bindir}/py-spy

%files
%doc README.md
%license LICENSE
%{_bindir}/py-spy

%changelog
%autochangelog
