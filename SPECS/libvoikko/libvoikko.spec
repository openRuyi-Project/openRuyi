# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libvoikko
Version:        4.3.3
Release:        %autorelease
Summary:        Voikko is a library for spellcheckers and hyphenators
License:        GPL-2.0-or-later
URL:            https://voikko.puimula.org/
VCS:            git:https://github.com/voikko/corevoikko
#!RemoteAsset
Source0:        https://www.puimula.org/voikko-sources/libvoikko/libvoikko-%{version}.tar.gz
#!RemoteAsset
Source1:        https://www.puimula.org/voikko-sources/libvoikko/libvoikko-%{version}.tar.gz.asc
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --enable-hfst=false
BuildOption(conf):  --with-dictionary-path=%{_datadir}/voikko

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  python3-devel

%description
Libvoikko is a library of free natural language processing tools. It
aims to provide support for languages that are not well served by
other existing free linguistic tools.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for developing
applications that use %{name}.

%package     -n python-libvoikko
Summary:        Python interface to %{name}
Provides:       python3-%{srcname}
%python_provide python3-%{srcname}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description -n python-libvoikko
Python interface to libvoikko, library of Finnish language tools.
This module can be used to perform various natural language analysis
tasks on Finnish text.

%conf -p
autoreconf -fiv

%install -a
install -d %{buildroot}/%{python3_sitelib}
install -pm 0644 python/libvoikko.py %{buildroot}/%{python3_sitelib}/

%files
%license COPYING
%doc ChangeLog README
%{_bindir}/voikkogc
%{_bindir}/voikkohyphenate
%{_bindir}/voikkospell
%{_bindir}/voikkovfstc
%{_libdir}/libvoikko.so.*
%{_mandir}/man1/voikkohyphenate.1*
%{_mandir}/man1/voikkospell.1*
%{_mandir}/man1/voikkogc.1*
%{_mandir}/man1/voikkovfstc.1*

%files devel
%{_includedir}/libvoikko
%{_libdir}/libvoikko.so
%{_libdir}/pkgconfig/libvoikko.pc

%files -n python-libvoikko
%{python3_sitelib}/*

%changelog
%autochangelog
