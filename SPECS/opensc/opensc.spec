# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           opensc
Version:        0.26.1
Release:        %autorelease
Summary:        Smart card library and applications
License:        LGPL-2.1-or-later AND BSD-3-Clause
URL:            https://github.com/OpenSC/OpenSC
#!RemoteAsset
Source0:        https://github.com/OpenSC/OpenSC/archive/refs/tags/%{version}.tar.gz
Source1:        opensc.module
BuildSystem:    autotools

# Disable PIN-pad by default.
Patch0:         0001-opensc-0.19.0-pinpad.patch
# Disable cache bacause cache brings trouble.
Patch1:         0002-opensc-0.22.0-file-cache.patch
# Fix C23 and GCC 14 build errors.
Patch2:         0003-opensc-0.26.1-compiler.patch
# Fix bash completion function name.
Patch3:         0004-opensc-0.26.1-bash-completion.patch

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-autostart-items
BuildOption(conf):  --disable-notify
BuildOption(conf):  --disable-assert
BuildOption(conf):  --enable-pcsc
BuildOption(conf):  --disable-cmocka
BuildOption(conf):  --enable-sm
BuildOption(conf):  --disable-tests
BuildOption(conf):  CFLAGS="%{optflags} -Wstrict-aliasing=2 -Wno-deprecated-declarations"

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libpcsclite)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  bash-completion
BuildRequires:  libxslt

Requires:       %{name}-libs = %{version}-%{release}
Requires:       pcsc-lite

%description
OpenSC provides a set of libraries and utilities to work with smart cards.

%package        libs
Requires:       pcsc-lite%{?_isa}
Summary:        OpenSC libraries

%description    libs
OpenSC libraries.

%prep -a
XFAIL_TESTS="test-pkcs11-tool-test-threads.sh test-pkcs11-tool-test.sh"

# In FIPS mode, OpenSSL doesn't allow RSA-PKCS, this is hardcoded into OpenSSL
# and we cannot influence it. Hence, the test is expected to fail in FIPS mode.
if [[ -f "/proc/sys/crypto/fips_enabled" && $(cat /proc/sys/crypto/fips_enabled) == "1" ]]; then
	XFAIL_TESTS+=" test-pkcs11-tool-unwrap-wrap-test.sh"
fi
sed -i -e "/XFAIL_TESTS/,$ {
  s/XFAIL_TESTS.*/XFAIL_TESTS=$XFAIL_TESTS/
  q
}" tests/Makefile.am

cp -p src/pkcs15init/README ./README.pkcs15init
cp -p src/scconf/README.scconf .

# No {_libdir} here to avoid multilib conflicts; it's just an example
sed -i -e 's|/usr/local/towitoko/lib/|/usr/lib/ctapi/|' etc/opensc.conf.example.in

%conf -p
autoreconf -fiv

%install -a
install -Dpm 644 %{SOURCE1} %{buildroot}%{_datadir}/p11-kit/modules/opensc.module

rm -rf %{buildroot}%{_datadir}/doc/opensc

# Upstream considers libopensc API internal and no longer ships
# public headers and pkgconfig files.
# Remove the symlink as nothing is supposed to link against libopensc.
rm -f %{buildroot}%{_libdir}/libopensc.so
rm -f %{buildroot}%{_libdir}/pkgconfig/*.pc
rm -f %{buildroot}%{_libdir}/libsmm-local.so

rm -rf %{buildroot}%{_bindir}/pkcs11-register
rm -rf %{buildroot}%{_mandir}/man1/pkcs11-register.1*
rm -rf %{buildroot}%{_datadir}/applications/org.opensc.notify.desktop
rm -rf %{buildroot}%{_mandir}/man1/opensc-notify.1*

%files
%doc COPYING NEWS README*
%{_sysconfdir}/bash_completion.d/*
%{_bindir}/*-tool
%{_bindir}/eidenv
%{_bindir}/opensc-asn1
%{_bindir}/opensc-explorer
%{_bindir}/pkcs15-crypt
%{_bindir}/pkcs15-init
%{_datadir}/opensc/

%files libs
%config(noreplace) %{_sysconfdir}/opensc.conf
# p11-kit module
%dir %{_datadir}/p11-kit
%dir %{_datadir}/p11-kit/modules
%{_datadir}/p11-kit/modules/opensc.module
# Libraries
%{_libdir}/libopensc.so.*
%{_libdir}/libsmm-local.so.*
%{_libdir}/opensc-pkcs11.so
%{_libdir}/pkcs11-spy.so
%{_libdir}/onepin-opensc-pkcs11.so
%dir %{_libdir}/pkcs11
%{_libdir}/pkcs11/opensc-pkcs11.so
%{_libdir}/pkcs11/onepin-opensc-pkcs11.so
%{_libdir}/pkcs11/pkcs11-spy.so

%changelog
%autochangelog
