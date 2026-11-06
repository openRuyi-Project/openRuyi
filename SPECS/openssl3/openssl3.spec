# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Julian Zhu <julian.oe@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define ssletcdir %{_sysconfdir}/pki/tls/openssl3
%define sonum 3

%bcond lto 0
%if %{with lto}
%define _lto_cflags %{nil}
%endif

%global _test_target test

Name:           openssl3
Version:        3.6.5
Release:        %autorelease
Summary:        Cryptography and SSL/TLS Toolkit
License:        Apache-2.0
URL:            https://www.openssl.org/
VCS:            git:https://github.com/openssl/openssl.git
#!RemoteAsset:  sha256:a2157c2830efdec3788939b00c9b0638306d3f0bbb76dc4832ee503bb397df98
Source:         https://www.openssl.org/source/openssl-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(prep):  -n openssl-%{version}
BuildOption(install):  HTMLDIR=%{_datadir}/doc/%{name}/html
BuildOption(check):  LD_LIBRARY_PATH="$PWD"

BuildRequires:  jitterentropy-devel
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(zlib)

%description
OpenSSL is a software library to be used in applications that need to
secure communications over computer networks against eavesdropping or
need to ascertain the identity of the party at the other end.
OpenSSL contains an implementation of the SSL and TLS protocols.

%package        devel
Summary:        Development files for building with OpenSSL
Requires:       %{name}%{?_isa} = %{version}-%{release}
Conflicts:      openssl-devel >= 4.0

%patchlist
# Use the shared jitterentropy library instead of static
0001-openssl-shared-jitterentropy.patch
# https://github.com/openssl/openssl/pull/30787
0004-RISC-V-Port-dot-asm-ChaCha20-assembly-implementation.patch
# https://github.com/openssl/openssl/pull/31178
0005-RISC-V-GHASH-multi-block-aggregation.patch
0006-RISC-V-GHASH-Zvbc-multi-block-aggregation.patch
0007-RISC-V-GHASH-Zvkg-multi-block-aggregation.patch
# https://github.com/openssl/openssl/pull/28673
0008-Backport-Instruction-rearrangement-optimization-for-SHA256-on-RISCV.patch
# https://github.com/openssl/openssl/pull/30194
0009-Backport-riscv-AES-XTS-Code-Comment-Correction.patch
# https://github.com/openssl/openssl/pull/29134
# https://github.com/openssl/openssl/pull/29137
# https://github.com/openssl/openssl/pull/29451
# https://github.com/openssl/openssl/pull/29544
0010-Backport-riscv-Performance-Optimization-of-SM4-CBC-on-RISC-V-Architecture.patch
# https://github.com/openssl/openssl/pull/31116
0011-Backport-riscv-Further-improve-the-decryption-performance-of-AES-128-CBC-on-RISC-V.patch
# https://github.com/openssl/openssl/pull/25918
0012-Add-SM2-implementation-in-generic-riscv64-asm.patch

%description    devel
This package contains the header files, pkgconfig/cmake files, development
symlinks, and API documentation needed to develop applications which will
use OpenSSL.

%package        doc
Summary:        HTML documentation for OpenSSL
BuildArch:      noarch

%description    doc
This package contains the HTML version of the API documentation and man
pages for OpenSSL.

%prep -a
# Keep providers linked against OpenSSL 3 out of the OpenSSL 4 module path.
sed -i 's|^MODULESDIR=$(libdir)/ossl-modules$|MODULESDIR=$(libdir)/ossl-modules-%{sonum}|' Configurations/unix-Makefile.tmpl
grep -Fx 'MODULESDIR=$(libdir)/ossl-modules-%{sonum}' Configurations/unix-Makefile.tmpl

%conf
./Configure \
    --prefix=%{_prefix} \
    --libdir=%{_lib} \
    --openssldir=%{ssletcdir} \
    shared \
    enable-camellia \
    enable-seed \
    enable-ec_nistp_64_gcc_128 \
    enable-jitter \
    enable-ktls \
    enable-rfc3779 \
    no-afalgeng \
    no-atexit \
    no-ec2m \
    no-mdc2 \
    zlib \
    enable-pie \
    %{optflags} \
    -Wa,--noexecstack \
    -Wl,-z,relro,-z,now \
    -Wall \
    -fno-common \
    -DTERMIOS \
    -D_GNU_SOURCE \
    -DOPENSSL_PEDANTIC_ZEROIZATION \
    -DOPENSSL_NO_BUF_FREELISTS \
    $(getconf LFS_CFLAGS)


sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' Makefile
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' Makefile

%check -p
export MALLOC_CHECK_=3
export MALLOC_PERTURB_=$(($RANDOM % 255 + 1))
export HARNESS_VERBOSE=yes
export HARNESS_JOBS=%{_ncpus}


%install -a
# Give the compatibility development package distinct pkg-config identities.
for pc in openssl libcrypto libssl; do
    mv %{buildroot}%{_libdir}/pkgconfig/${pc}.pc %{buildroot}%{_libdir}/pkgconfig/${pc}3.pc
done
sed -i 's/^Requires: libssl libcrypto$/Requires: libssl3 libcrypto3/' %{buildroot}%{_libdir}/pkgconfig/openssl3.pc
sed -i 's/^Requires.private: libcrypto$/Requires.private: libcrypto3/' %{buildroot}%{_libdir}/pkgconfig/libssl3.pc

# Remove static libraries
rm -f %{buildroot}%{_libdir}/*.a
# Remove the cnf.dist
rm -f %{buildroot}%{ssletcdir}/openssl.cnf.dist
rm -f %{buildroot}%{ssletcdir}/ct_log_list.cnf.dist

# Create the compatibility symlink for older software.
ln -sf ./openssl %{buildroot}/%{_includedir}/ssl

# Share system trust anchors, while keeping the configuration private to 3.x.
rm -rf %{buildroot}%{ssletcdir}/certs
ln -s ../certs %{buildroot}%{ssletcdir}/certs

# The system OpenSSL package owns command-line tools and user manuals.
rm -f %{buildroot}%{_bindir}/openssl %{buildroot}%{_bindir}/c_rehash
rm -rf %{buildroot}%{ssletcdir}/misc
rm -rf %{buildroot}%{_mandir}/man1 %{buildroot}%{_mandir}/man5 %{buildroot}%{_mandir}/man7

# Do not install demo scripts executable under /usr/share/doc
find demos -type f -perm /111 -exec chmod 644 {} +

%files
%license LICENSE.txt
%doc NEWS.md README.md
# Runtime libraries
%{_libdir}/libcrypto.so.%{sonum}
%{_libdir}/libssl.so.%{sonum}
# Engines and modules
%{_libdir}/engines-3/
%{_libdir}/ossl-modules-%{sonum}/
%dir %{ssletcdir}
%{ssletcdir}/certs
# Configuration files and directories
%attr(700,root,root) %{ssletcdir}/private
%config (noreplace) %{ssletcdir}/openssl.cnf
%config (noreplace) %{ssletcdir}/ct_log_list.cnf

%files devel
# Header files
%{_includedir}/openssl/
%{_includedir}/ssl
# Development symlinks
%{_libdir}/libcrypto.so
%{_libdir}/libssl.so
# Build system support files (pkg-config and CMake)
%{_libdir}/pkgconfig/openssl3.pc
%{_libdir}/pkgconfig/libcrypto3.pc
%{_libdir}/pkgconfig/libssl3.pc
%dir %{_libdir}/cmake
%dir %{_libdir}/cmake/OpenSSL
%{_libdir}/cmake/OpenSSL/*.cmake
# API documentation (man3)
%{_mandir}/man3/*

%files doc
%{_datadir}/doc/%{name}/html/

%changelog
%autochangelog
