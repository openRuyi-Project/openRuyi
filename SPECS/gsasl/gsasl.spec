# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           gsasl
Version:        2.2.2
Release:        %autorelease
Summary:        GNU SASL library
License:        LGPL-2.1-or-later
URL:            https://www.gnu.org/software/gsasl/
VCS:            git:https://gitlab.com/gsasl/gsasl
#!RemoteAsset
Source0:        https://ftpmirror.gnu.org/gnu/gsasl/%{name}-%{version}.tar.gz
#!RemoteAsset
Source1:        https://ftpmirror.gnu.org/gnu/gsasl/%{name}-%{version}.tar.gz.sig
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-rpath
BuildOption(conf):  --with-gssapi-impl=mit

BuildRequires:  gcc
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(libidn2)
BuildRequires:  pkgconfig
BuildRequires:  gettext

%description
The GNU SASL library includes support for the SASL framework and various
mechanisms like CRAM-MD5, EXTERNAL, GSSAPI, ANONYMOUS, PLAIN, DIGEST-MD5,
LOGIN, and NTLM.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
This package contains libraries and header files for developing applications
that use the GNU SASL library.

%install -a
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
%autochangelog
