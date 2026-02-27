# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Ruoqing He <heruoqing@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define __spec_install_post %{nil}
%global debug_package %{nil}

%ifarch riscv64
%global rust_arch riscv64gc
%else
%global rust_arch %{_arch}
%endif

Name:           rust-bin
Version:        1.94.1
Release:        %autorelease
Summary:        A systems programming language
License:        Apache-2.0 OR MIT
URL:            https://forge.rust-lang.org/infra/other-installation-methods.html#standalone
#!RemoteAsset
Source0:        https://static.rust-lang.org/dist/rust-%{version}-riscv64gc-unknown-linux-gnu.tar.gz
#!RemoteAsset
Source1:        https://static.rust-lang.org/dist/rust-%{version}-x86_64-unknown-linux-gnu.tar.gz
ExclusiveArch:  riscv64 x86_64

BuildRequires:  bash
BuildRequires:  tar
BuildRequires:  gzip

Provides:       rust = %{version}-%{release}
Provides:       rust%{?_isa} = %{version}-%{release}
Provides:       cargo = %{version}-%{release}
Provides:       cargo%{?_isa} = %{version}-%{release}

%description
Rust is a systems programming language focused on three goals: safety,
speed, and concurrency.

⚠️  This is the Rust toolchain intended for build pipelines. If you
want to install Rust for a development environment, you should install
'rustup' instead.

%prep
tar xf %{_sourcedir}/rust-%{version}-%{rust_arch}-unknown-linux-gnu.tar.gz --strip-components=1

%build

%install
./install.sh --prefix=%{buildroot}/%{_prefix} --components=rustc,cargo,rust-std-%{rust_arch}-unknown-linux-gnu
mv %{buildroot}%{_prefix}%{_sysconfdir} %{buildroot}
rm %{buildroot}%{_prefix}/lib/rustlib/install.log
rm %{buildroot}%{_prefix}/lib/rustlib/manifest-*

%files
%defattr(-,root,root,-)
%{_bindir}/*{cargo,rust}*
%{_sysconfdir}/bash_completion.d/cargo
%{_mandir}/man1/{cargo,rust}*
%{_datadir}/doc/{cargo,rust}
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_cargo
%dir %{_prefix}/libexec
%{_prefix}/libexec/*
%{_prefix}/lib/rustlib
%{_prefix}/lib/*.so
%ifarch x86_64
%{_prefix}/lib/libLLVM.so.*-rust-%{version}-stable
%endif
%exclude %{_sysconfdir}/target-spec-json-schema.json
%changelog
%{?autochangelog}
