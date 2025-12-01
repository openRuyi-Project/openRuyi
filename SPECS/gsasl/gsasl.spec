# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           gsasl
Version:        2.2.2
Release:        %autorelease
Summary:        GNU SASL library
License:        LGPL-2.1-or-later
URL:            https://www.gnu.org/software/gsasl/
#!RemoteAsset
Source0:        https://ftpmirror.gnu.org/gnu/gsasl/%{name}-%{version}.tar.gz
#!RemoteAsset
Source1:        https://ftpmirror.gnu.org/gnu/gsasl/%{name}-%{version}.tar.gz.sig

BuildSystem:    autotools

BuildOption(conf): --disable-static
BuildOption(conf): --disable-rpath
BuildOption(conf): --with-gssapi-impl=mit

BuildRequires:  gcc krb5-devel libgcrypt-devel libidn2-devel pkgconfig gettext

%description
The GNU SASL library includes support for the SASL framework and various
mechanisms like CRAM-MD5, EXTERNAL, GSSAPI, ANONYMOUS, PLAIN, DIGEST-MD5,
LOGIN, and NTLM.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}
Requires:       pkgconfig

%description    devel
This package contains libraries and header files for developing applications
that use the GNU SASL library.


%install -a
find %{buildroot} -name '*.la' -exec rm -f {} ';'
%find_lang %{name} --generate-subpackages

%files
%doc AUTHORS NEWS README THANKS
%license COPYING
%{_bindir}/gsasl
%{_libdir}/libgsasl.so.*

%files devel
%{_includedir}/gsasl*
%{_libdir}/libgsasl.so
%{_libdir}/pkgconfig/libgsasl.pc
%{_infodir}/gsasl.info*
%{_mandir}/man1/gsasl.*
%{_mandir}/man3/gsasl*.3*

%changelog
%{?autochangelog}
