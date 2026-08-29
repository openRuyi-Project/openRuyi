# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# We don't have asciidoctor packaged - 251
# If we have it in the future, change to 1
%bcond asciidoc 0

%global upstream_main_version 2.8

Name:           cryptsetup
Version:        %{upstream_main_version}.6
Release:        %autorelease
Summary:        Utility for setting up encrypted disks
License:        GPL-2.0-or-later WITH cryptsetup-OpenSSL-exception AND LGPL-2.1-or-later WITH cryptsetup-OpenSSL-exception
URL:            https://gitlab.com/cryptsetup/cryptsetup
#!RemoteAsset:  sha256:8004265fd993885d08f7b633dbe056851de1a210307613a4ebddc743fccefe5a
Source0:        https://cdn.kernel.org/pub/linux/utils/cryptsetup/v%{upstream_main_version}/cryptsetup-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --enable-fips
BuildOption(conf):  --enable-pwquality
%if %{with asciidoc}
BuildOption(conf):  --enable-asciidoc
%else
BuildOption(conf):  --disable-asciidoc
%endif
BuildOption(conf):  --enable-internal-sse-argon2

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(popt)
# We need libuuid.so also uuid.h - 251
BuildRequires:  util-linux-devel
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(pwquality)
BuildRequires:  libblkid
BuildRequires:  pkgconfig(libssh)
BuildRequires:  make
BuildRequires:  device-mapper-devel
%if %{with asciidoc}
BuildRequires:  asciidoctor
%endif

Requires:       cryptsetup-libs = %{version}-%{release}
Requires:       libpwquality
Provides:       %{name}-reencrypt = %{version}

%description
The cryptsetup package contains a utility for setting up
disk encryption using dm-crypt kernel module.

%package        devel
Requires:       %{name}-libs = %{version}-%{release}
Requires:       pkgconfig(libudev)
Summary:        Headers and libraries for using encrypted file systems

%description    devel
The cryptsetup-devel package contains libraries and header files
used for writing code that makes use of disk encryption.

%package        libs
Summary:        Cryptsetup shared library

%description    libs
This package contains the cryptsetup shared library, libcryptsetup.

%package        ssh
Summary:        Cryptsetup LUKS2 SSH token
Requires:       cryptsetup-libs = %{version}-%{release}

%description    ssh
This package contains the LUKS2 SSH token.

%package     -n veritysetup
Summary:        A utility for setting up dm-verity volumes
Requires:       cryptsetup-libs = %{version}-%{release}

%description -n veritysetup
The veritysetup package contains a utility for setting up
disk verification using dm-verity kernel module.

%package     -n integritysetup
Summary:        A utility for setting up dm-integrity volumes
Requires:       cryptsetup-libs = %{version}-%{release}

%description -n integritysetup
The integritysetup package contains a utility for setting up
disk integrity protection using dm-integrity kernel module.

%prep -a
./autogen.sh

%install -a
%find_lang %{name} --generate-subpackages

%files -f %{name}.lang
%license COPYING
%doc AUTHORS FAQ.md docs/*ReleaseNotes
%{_mandir}/man8/cryptsetup.8.gz
%{_mandir}/man8/cryptsetup-*.8.gz
%{_sbindir}/cryptsetup

%files -n veritysetup
%license COPYING
%{_mandir}/man8/veritysetup.8.gz
%{_sbindir}/veritysetup

%files -n integritysetup
%license COPYING
%{_mandir}/man8/integritysetup.8.gz
%{_sbindir}/integritysetup

%files devel
%doc docs/examples/*
%{_includedir}/libcryptsetup.h
%{_libdir}/libcryptsetup.so
%{_libdir}/pkgconfig/libcryptsetup.pc

%files libs
%license COPYING docs/licenses/COPYING.LGPL-2.1-or-later-WITH-cryptsetup-OpenSSL-exception
%{_libdir}/libcryptsetup.so.*
%dir %{_libdir}/cryptsetup/
%{_tmpfilesdir}/cryptsetup.conf
%ghost %attr(700, -, -) %dir /run/cryptsetup

%files ssh
%license COPYING docs/licenses/COPYING.LGPL-2.1-or-later-WITH-cryptsetup-OpenSSL-exception
%{_libdir}/cryptsetup/libcryptsetup-token-ssh.so
%{_mandir}/man8/cryptsetup-ssh.8.gz
%{_sbindir}/cryptsetup-ssh

%changelog
%autochangelog
