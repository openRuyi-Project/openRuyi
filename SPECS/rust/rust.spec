# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: YunQiang Su <yunqiang@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%ifarch x86_64
%global rust_arch x86_64-unknown-linux-gnu
%endif
%ifarch riscv64
%global rust_arch riscv64gc-unknown-linux-gnu
%endif

Name:           rust
Version:        1.91.1
Release:        %autorelease
Summary:        Rust systems programming language
License:        MIT AND Apache-2.0
URL:            http://www.rust-lang.org/
VCS:            git:https://github.com/rust-lang/rust.git
#!RemoteAsset
Source0:        https://static.rust-lang.org/dist/rustc-%{version}-src.tar.xz
Source1:        rust-openruyi.toml

# This patch make rustc build with unvendor sqlite
Patch0:         rustc-1.91.1-unbundle-sqlite.patch
# This patch make miri build with system libffi
Patch1:         rustc-miri-use-system-libffi.patch

BuildRequires:  clang
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  llvm-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libgit2)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  pkgconfig(oniguruma)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3
BuildRequires:  findutils
BuildRequires:  rust

Conflicts:      rust-bin

Provides:       cargo = %{version}-%{release}
Provides:       cargo%{?_isa} = %{version}-%{release}

%description
A language empowering everyone to build reliable and efficient software.

%prep
%autosetup -n rustc-%{version}-src -p1
find . -type d -path src/llvm-project ! -path "src/llvm-project/compiler-rt" -delete
# rm -rf vendor/lzma-sys-*/xz-*
rm -rf vendor/libdbus-sys*/vendor/dbus/
rm -rf vendor/libffi-sys*/libffi/
rm -rf vendor/libgit2-sys*/libgit2/
rm -rf vendor/libmimalloc-sys*/c_src/mimalloc/
rm -rf vendor/libsqlite3-sys*/sqlite3/
rm -rf vendor/libssh2-sys*/libssh2/
rm -rf vendor/libz-sys*/src/zlib{,-ng}/
rm -rf vendor/onig_sys*/oniguruma/
rm -rf vendor/openssl-src-*/openssl
rm -rf vendor/pcre2-sys-*/pcre2/

# TODO: unvendor jemalloc when we have it.
# rm -rf vendor/jemalloc-sys-*-patched/jemalloc
# rm -rf vendor/tikv-jemalloc-sys-0.5.4+5.3.0-patched/jemalloc
# rm -rf vendor/tikv-jemalloc-sys-0.6.0+5.3.0-1-ge13ca993e8ccb9ba9847cc330696e02839f328f7/jemalloc

find . -type f -regex  ".*\.\(exe\|a\|dll\|lib\)$" -delete
find vendor -name .cargo-checksum.json -exec sed -i.uncheck -e 's/"files":{[^}]*}/"files":{ }/' '{}' '+'
cp -f %{SOURCE1} .

%build
export RUSTONIG_SYSTEM_LIBONIG=1
export LIBSQLITE3_SYS_USE_PKG_CONFIG=1
export LIBSSH2_SYS_USE_PKG_CONFIG=1
export RUST_BACKTRACE=1
./x build --stage 2 --config %{SOURCE1} --target %{rust_arch}

%install
export RUSTONIG_SYSTEM_LIBONIG=1
export LIBSQLITE3_SYS_USE_PKG_CONFIG=1
export LIBSSH2_SYS_USE_PKG_CONFIG=1
export RUST_BACKTRACE=1
DESTDIR=%{buildroot} ./x.py install --config %{SOURCE1} --target %{rust_arch}
rm -rf %{buildroot}/usr/share/doc/docs
# rust-objcopy is a hard link to llvm-objcopy, so the conflict build-id.
strip --remove-section=.note.gnu.build-id %{buildroot}%{_prefix}/lib/rustlib/%{rust_arch}/bin/rust-objcopy

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
%autochangelog
