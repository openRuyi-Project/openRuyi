# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           wofi
Version:        1.5.2
Release:        %autorelease
Summary:        A launcher/menu program for wlroots based wayland compositors
License:        GPL-3.0-only
URL:            https://hg.sr.ht/~scoopta/wofi
#!RemoteAsset:  sha256:fa8a1e2937a94de2801bed2fe9c66225116be6d2f9dee8a237d7d76fa8ac1018
Source0:        https://hg.sr.ht/~scoopta/wofi/archive/v%{version}.tar.gz
BuildSystem:    meson

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(wayland-client)

%description
Wofi is a launcher/menu program for wlroots based wayland compositors such as
sway.

%package        devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Files for development with %{name}.

%files
%license COPYING.md
%doc README.md
%{_bindir}/wofi
%{_mandir}/man1/wofi.1*
%{_mandir}/man5/wofi.5*
%{_mandir}/man7/wofi-keys.7*
%{_mandir}/man7/wofi.7*

%files devel
%{_includedir}/wofi-1/*.h
%{_libdir}/pkgconfig/wofi.pc
%{_mandir}/man3/wofi*.3*

%changelog
%autochangelog
