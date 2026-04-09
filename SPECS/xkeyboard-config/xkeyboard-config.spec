# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global pkgconfig_name xkeyboard-config-2

Name:           xkeyboard-config
Version:        2.46
Release:        %autorelease
Summary:        X Keyboard Extension configuration data
License:        HPND AND HPND-sell-variant AND X11 AND MIT
URL:            https://gitlab.freedesktop.org/xkeyboard-config/xkeyboard-config
#!RemoteAsset
Source0:        http://xorg.freedesktop.org/archive/individual/data/xkeyboard-config/xkeyboard-config-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Dcompat-rules=true
BuildOption(conf):  -Dxorg-rules-symlinks=true

BuildRequires:  meson
BuildRequires:  gettext
BuildRequires:  libxslt
BuildRequires:  perl-XML-Parser
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xproto)

%description
This package contains configuration data used by the X Keyboard Extension (XKB),
which allows selection of keyboard layouts when using a graphical interface.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
Development files for %{name}.

%install -a
if [ -L %{buildroot}%{_datadir}/X11/xkb ]; then
    rm %{buildroot}%{_datadir}/X11/xkb
    ln -srf %{buildroot}%{_datadir}/%{pkgconfig_name} %{buildroot}%{_datadir}/X11/xkb
fi

if [ ! -e %{buildroot}%{_datadir}/X11/xkb ]; then
    mkdir -p %{buildroot}%{_datadir}/X11
    ln -srf %{buildroot}%{_datadir}/%{pkgconfig_name} %{buildroot}%{_datadir}/X11/xkb
fi

%find_lang %{name} --all-name --generate-subpackages

%files -f %{name}.lang
%doc AUTHORS README.md COPYING docs/README.* docs/HOWTO.*
%{_mandir}/man7/xkeyboard-config.*
%{_mandir}/man7/%{pkgconfig_name}.*
%{_datadir}/%{pkgconfig_name}/
%{_datadir}/X11/xkb

%files devel
%{_datadir}/pkgconfig/%{pkgconfig_name}.pc
%{_datadir}/pkgconfig/xkeyboard-config.pc

%changelog
%autochangelog
