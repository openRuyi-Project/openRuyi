# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond gtk 0

Name:           mtr
Version:        0.96
Release:        %autorelease
Summary:        Network diagnostic tool combining 'traceroute' and 'ping'
License:        GPL-2.0-or-later
URL:            https://www.bitwizard.nl/mtr/
VCS:            git:https://github.com/traviscross/mtr
#!RemoteAsset
Source0:        https://github.com/traviscross/mtr/archive/refs/tags/v%{version}.tar.gz
Source1:        net-xmtr.desktop

BuildSystem:    autotools

BuildOption(conf):  LIBS="-ltinfo"
%if %{with gtk}
BuildOption(conf):  --with-gtk
%else
BuildOption(conf):  --without-gtk
%endif

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(jansson)

%if %{with gtk}
BuildRequires:  gtk3-devel
BuildRequires:  desktop-file-utils
%endif

%description
MTR combines the functionality of the 'traceroute' and 'ping' programs
in a single network diagnostic tool.

%if %{with gtk}
%package        gtk
Summary:        GTK interface for MTR
Requires:       %{name} = %{version}-%{release}

%description    gtk
The mtr-gtk package provides the GTK interface for MTR.
%endif

%conf -p
./bootstrap.sh

%install -a
%if %{with gtk}
install -D -p -m 0644 img/mtr_icon.xpm %{buildroot}%{_datadir}/pixmaps/mtr_icon.xpm
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
%endif

# tests require network access
%check

%files
%license COPYING
%doc AUTHORS FORMATS NEWS README.md SECURITY
%{_sbindir}/mtr
%attr(0755,root,root) %caps(cap_net_raw=pe) %{_sbindir}/mtr-packet
%{_mandir}/man8/mtr.8*
%{_mandir}/man8/mtr-packet.8*
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/mtr

%if %{with gtk}
%files gtk
%{_bindir}/xmtr
%{_datadir}/pixmaps/mtr_icon.xpm
%{_datadir}/applications/net-xmtr.desktop
%endif

%changelog
%autochangelog
