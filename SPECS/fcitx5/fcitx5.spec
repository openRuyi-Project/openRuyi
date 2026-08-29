# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global __provides_exclude_from ^%{_libdir}/%{name}/.*\\.so$
%global _xinputconf %{_sysconfdir}/X11/xinit/xinput.d/fcitx5.conf

Name:           fcitx5
Version:        5.1.19
Release:        %autorelease
Summary:        Next generation of fcitx input method framework
License:        LGPL-2.1-or-later
URL:            https://github.com/fcitx/fcitx5
#!RemoteAsset:  sha256:80dde9d38a57993eb90df89a1d52ca479af2de4864d6360c4fc9f3dc7053fad9
Source0:        https://download.fcitx-im.org/fcitx5/fcitx5/fcitx5-%{version}_dict.tar.zst
Source1:        fcitx5-xinput
Source2:        fcitx5.sh
BuildSystem:    cmake

BuildRequires:  appstream
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  ninja
BuildRequires:  cmake(nlohmann_json)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-xcb)
BuildRequires:  pkgconfig(cldr-emoji-annotation)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(enchant-2)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-imdkit)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xkeyboard-config)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xkbfile)

%description
Fcitx 5 is a generic input method framework released under LGPL-2.1+.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files necessary for
developing programs using Fcitx5 libraries.

%install -a
install -pm 644 -D %{SOURCE1} %{buildroot}%{_xinputconf}
install -pm 644 -D %{SOURCE2} %{buildroot}%{_sysconfdir}/profile.d/fcitx5.sh
install -d %{buildroot}%{_datadir}/%{name}/inputmethod
install -d %{buildroot}%{_datadir}/%{name}/table

desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}-configtool.desktop

desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/org.fcitx.Fcitx5.desktop

desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}-wayland-launcher.desktop

# Convert symlinked icons to copied icons, for co-existing with fcitx4
for iconfile in $(find %{buildroot}%{_datadir}/icons -type l)
do
  origicon=$(readlink -f ${iconfile})
  rm -f ${iconfile}
  cp ${origicon} ${iconfile}
done

# Rename en_dict to match what fcitx5 expects
mv %{buildroot}%{_datadir}/%{name}/dict/en_dict-* %{buildroot}%{_datadir}/%{name}/dict/en_dict.tar.gz 2>/dev/null || :

%find_lang %{name} --generate-subpackages

%files -f %{name}.lang
%doc README.md
%license LICENSES/LGPL-2.1-or-later.txt
%config %{_xinputconf}
%{_bindir}/%{name}
%{_bindir}/%{name}-configtool
%{_bindir}/%{name}-remote
%{_bindir}/%{name}-diagnose
%{_libdir}/%{name}/
%{_libdir}/libFcitx5*.so.*
%{_libexecdir}/fcitx5-wayland-launcher
%{_sysconfdir}/xdg/Xwayland-session.d/20-fcitx-x11
%config %{_sysconfdir}/xdg/autostart/org.fcitx.Fcitx5.desktop
%config %{_sysconfdir}/profile.d/fcitx5.sh
%{_datadir}/%{name}
%{_datadir}/dbus-1/services/org.fcitx.Fcitx5.service
%{_datadir}/applications/org.fcitx.Fcitx5.desktop
%{_datadir}/metainfo/org.fcitx.Fcitx5.metainfo.xml
%{_datadir}/applications/%{name}-configtool.desktop
%{_datadir}/applications/%{name}-wayland-launcher.desktop
%{_datadir}/icons/hicolor/*/apps/*

%files devel
%{_includedir}/Fcitx5/
%{_libdir}/cmake/Fcitx5*/
%{_libdir}/libFcitx5*.so
%{_libdir}/pkgconfig/Fcitx5*.pc

%changelog
%autochangelog
