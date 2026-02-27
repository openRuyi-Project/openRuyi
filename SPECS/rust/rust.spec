# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: YunQiang Su <yunqiang@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond rust_bin 0

%ifarch x86_64
%global rust_arch x86_64-unknown-linux-gnu
%endif
%ifarch riscv64
%if "%{openruyi_riscv_arch}" == "-march=rva23u64"
%global rust_arch riscv64a23-unknown-linux-gnu
%else
%global rust_arch riscv64gc-unknown-linux-gnu
%endif
%endif

# We might use rust-rv64gc to bootstrap rust-rva23u64.
# PKG_CONFIG_ALLOW_CROSS let pkg-config work in this
# special "cross-compile" scenario.
%global rust_env PKG_CONFIG_ALLOW_CROSS=1
%global rust_env %{rust_env} RUSTONIG_SYSTEM_LIBONIG=1
%global rust_env %{rust_env} LIBSSH2_SYS_USE_PKG_CONFIG=1
%global rust_env %{rust_env} RUST_BACKTRACE=1

Name:           rust
Version:        1.94.1
Release:        %autorelease
Summary:        Rust systems programming language
License:        MIT AND Apache-2.0
URL:            http://www.rust-lang.org/
VCS:            git:https://github.com/rust-lang/rust.git
#!RemoteAsset
Source0:        https://static.rust-lang.org/dist/rustc-%{version}-src.tar.xz
Source1:        rust-openruyi.toml

BuildRequires:  clang
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  llvm-devel
BuildRequires:  compiler-rt
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libgit2) >= 1.9.2
BuildRequires:  pkgconfig(libgit2) < 1.10.0
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  pkgconfig(oniguruma)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3
BuildRequires:  findutils
%if %{with rust_bin}
BuildRequires:  rust-bin >= 1.93.0
%else
BuildRequires:  rust >= 1.93.0
%endif
# For tests.
BuildRequires:  git-core
BuildRequires:  gdb
BuildRequires:  glibc-static
BuildRequires:  procps-ng

Conflicts:      rust-bin

Provides:       cargo = %{version}-%{release}
Provides:       cargo%{?_isa} = %{version}-%{release}

%description
A language empowering everyone to build reliable and efficient software.

%prep
%autosetup -n rustc-%{version}-src -p1
# `rust-src` installer needs this dir but we dont want to package it.
rm -rf src/llvm-project/libunwind/*

find . -type f -regex  ".*\.\(exe\|a\|dll\|lib\)$" -delete
find vendor -name .cargo-checksum.json -exec sed -i.uncheck -e 's/"files":{[^}]*}/"files":{ }/' '{}' '+'
sed 's/CLANG-MAJOR-VERSION/%{clang_major_version}/' %{SOURCE1} > bootstrap.toml

%build
export %{rust_env}
./x build --target %{rust_arch} --host %{rust_arch}

%install
export %{rust_env}
DESTDIR=%{buildroot} ./x.py install --target %{rust_arch} --host %{rust_arch}
rm -rf %{buildroot}/usr/share/doc/docs

%check
export %{rust_env}
# Exclude this test due to our llvm has no arm target.
./x.py test --no-fail-fast --target %{rust_arch} --host %{rust_arch} \
            --exclude tests/run-make/rustdoc-target-modifiers || :
# Skip these 2 tests due to no network access.
./x.py test --no-fail-fast --target %{rust_arch} --host %{rust_arch} cargo \
            --test-args '--skip net_err_suggests_fetch_with_cli --skip publish_to_crates_io_warns' || :
./x.py test --no-fail-fast --target %{rust_arch} --host %{rust_arch} clippy || :
./x.py test --target %{rust_arch} --host %{rust_arch} rust-analyzer
./x.py test --target %{rust_arch} --host %{rust_arch} rustfmt

%files
%license COPYRIGHT LICENSE-APACHE LICENSE-MIT
%doc %{_defaultdocdir}/*
%{_bindir}/*
%{_prefix}/lib/*.so
%{_prefix}/lib/rustlib/*
%{_libexecdir}/*
%{_mandir}/man1/*
%{_datadir}/zsh/site-functions/*
%{_sysconfdir}/bash_completion.d/*
%exclude %{_sysconfdir}/target-spec-json-schema.json

%changelog
%{?autochangelog}
