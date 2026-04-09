# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define ssletcdir %{_sysconfdir}/pki/tls
%define sonum 3

%bcond lto 0
%if %{with lto}
%define _lto_cflags %{nil}
%endif

%global _test_target test

Name:           openssl
Version:        3.5.2
Release:        %autorelease
Summary:        Cryptography and SSL/TLS Toolkit
License:        Apache-2.0
URL:            https://www.openssl.org/
VCS:            git:https://github.com/openssl/openssl.git
#!RemoteAsset
Source:         https://www.openssl.org/source/%{name}-%{version}.tar.gz
BuildSystem:    autotools

# Use the shared jitterentropy library instead of static
Patch0:         openssl-shared-jitterentropy.patch

BuildOption(check):  LD_LIBRARY_PATH="$PWD"

BuildRequires:  gcc
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
# Remove static libraries
rm -f %{buildroot}%{_libdir}/*.a
# Remove the cnf.dist
rm -f %{buildroot}%{ssletcdir}/openssl.cnf.dist
rm -f %{buildroot}%{ssletcdir}/ct_log_list.cnf.dist

# Create the compatibility symlink for older software.
ln -sf ./%{name} %{buildroot}/%{_includedir}/ssl

# Relocate misc scripts to /usr/share, keeping /etc clean.
mkdir %{buildroot}/%{_datadir}/ssl
mv %{buildroot}/%{ssletcdir}/misc %{buildroot}/%{_datadir}/ssl/

# Do not install demo scripts executable under /usr/share/doc
find demos -type f -perm /111 -exec chmod 644 {} +

%files
%license LICENSE.txt
%doc NEWS.md README.md
# Runtime libraries
%{_libdir}/libcrypto.so.%{sonum}
%{_libdir}/libssl.so.%{sonum}
# Command-line tool
%{_bindir}/openssl
%{_bindir}/c_rehash
# Engines and modules
%{_libdir}/engines-3/
%{_libdir}/ossl-modules/
%dir %{ssletcdir}
# Configuration files and directories
%attr(700,root,root) %{ssletcdir}/private
%config (noreplace) %{ssletcdir}/openssl.cnf
%config (noreplace) %{ssletcdir}/ct_log_list.cnf
# User-level man pages
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man7/*

%files devel
# Header files
%{_includedir}/openssl/
%{_includedir}/ssl
# Development symlinks
%{_libdir}/libcrypto.so
%{_libdir}/libssl.so
# Build system support files (pkg-config and CMake)
%{_libdir}/pkgconfig/openssl.pc
%{_libdir}/pkgconfig/libcrypto.pc
%{_libdir}/pkgconfig/libssl.pc
%dir %{_libdir}/cmake
%dir %{_libdir}/cmake/OpenSSL
%{_libdir}/cmake/OpenSSL/*.cmake
# API documentation (man3)
%{_mandir}/man3/*
%dir %{_datadir}/ssl
%{_datadir}/ssl/misc

%files doc
%{_datadir}/doc/openssl/html/

%changelog
%autochangelog
