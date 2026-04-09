# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Dingli Zhang <dingli@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           fontconfig
Version:        2.17.1
Release:        %autorelease
Summary:        Font configuration and customization library
License:        HPND AND LicenseRef-openRuyi-Public-Domain AND Unicode-DFS-2016
URL:            https://www.freedesktop.org/wiki/Software/fontconfig/
VCS:            git:https://gitlab.freedesktop.org/fontconfig/fontconfig
#!RemoteAsset
Source:         https://gitlab.freedesktop.org/fontconfig/fontconfig/-/archive/%{version}/fontconfig-%{version}.tar.gz

BuildSystem:    meson

BuildOption(conf):  -Ddoc-pdf=disabled
BuildOption(conf):  -Ddoc-txt=disabled
BuildOption(conf):  -Dxml-backend=libxml2
BuildOption(conf):  --default-library=shared
BuildOption(conf):  -Dtemplate-dir=%{_datadir}/%{name}/conf.avail
BuildOption(conf):  -Dconfig-dir=%{_sysconfdir}/fonts/conf.d
BuildOption(conf):  -Dbaseconfig-dir=%{_datadir}/fonts
BuildOption(conf):  -Dcache-dir=/var/cache/fontconfig

BuildRequires:  gcc
BuildRequires:  gperf
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  docbook-utils
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(json-c)

%description
Fontconfig is a library designed to locate fonts within the system and select
them according to requirements specified by applications. This package contains
the runtime library and essential command-line tools.

%package        devel
Summary:        Development files for fontconfig
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(freetype2)

%description    devel
This package includes the header files, pkgconfig files, and developer docs
for the fontconfig library. Install it if you want to develop programs that
use fontconfig.

%package        doc
Summary:        Documentation for fontconfig
BuildArch:      noarch

%description    doc
Contains detailed user and developer documentation for fontconfig.

%install -a
# Create required config and cache directories, and add a symbolic link.
# This keeps system-wide configuration consistent with upstream fontconfig layout,
# ensuring all applications reference the same canonical fonts.conf location.
install -d -m 755 %{buildroot}%{_sysconfdir}/fonts
install -d -m 755 %{buildroot}%{_localstatedir}/cache/fontconfig
ln -sf ../../usr/share/fonts/fonts.conf %{buildroot}%{_sysconfdir}/fonts/fonts.conf
%find_lang %{name} --generate-subpackages --all-name

%pretrans
mkdir -p %{_localstatedir}/cache/fontconfig

%post
if [ "$1" -eq 1 ]; then
    rm -rf %{_localstatedir}/cache/fontconfig/* 2>/dev/null || :
fi
%{_bindir}/fc-cache -fs

%postun
if [ $1 -eq 0 ]; then
    rm -rf %{_localstatedir}/cache/fontconfig
fi

%posttrans
if [ -e %{_sysconfdir}/xml/catalog ]; then
    %{_bindir}/xmlcatalog --noout --add system \
        "urn:fontconfig:fonts.dtd" \
        "file://%{_datadir}/xml/fontconfig/fonts.dtd" \
        %{_sysconfdir}/xml/catalog
fi

%postuntrans
if [ $1 -eq 0 ] && [ -e %{_sysconfdir}/xml/catalog ]; then
    %{_bindir}/xmlcatalog --noout --del "urn:fontconfig:fonts.dtd" %{_sysconfdir}/xml/catalog
fi

%transfiletriggerin -- /usr/share/fonts
%{_bindir}/fc-cache -s

%transfiletriggerpostun -- /usr/share/fonts
%{_bindir}/fc-cache -s

%files
%license COPYING
%doc README.md AUTHORS
%{_bindir}/fc-*
%{_libdir}/libfontconfig.so.*
%dir %{_datadir}/fontconfig
%{_datadir}/fontconfig/conf.avail/
%{_datadir}/fonts/fonts.conf
%dir %{_sysconfdir}/fonts
%dir %{_sysconfdir}/fonts/conf.d
%config(noreplace) %{_sysconfdir}/fonts/conf.d/*.conf
%{_sysconfdir}/fonts/conf.d/README
%{_sysconfdir}/fonts/fonts.conf
%{_datadir}/xml/fontconfig/
%dir %{_localstatedir}/cache/fontconfig
%{_mandir}/man1/fc-*.1*
%{_mandir}/man5/fonts-conf.5*
%{_datadir}/gettext/its/fontconfig.its
%{_datadir}/gettext/its/fontconfig.loc

%files devel
%{_libdir}/libfontconfig.so
%{_libdir}/pkgconfig/fontconfig.pc
%{_includedir}/fontconfig/
%{_mandir}/man3/Fc*.3*

%files doc
%doc %{_docdir}/%{name}/fontconfig-*.html

%changelog
%autochangelog
