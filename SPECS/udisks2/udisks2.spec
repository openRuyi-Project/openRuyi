# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond iscsi 0
%bcond lsm 0
%bcond doc 0

Name:           udisks2
Version:        2.11.0
Release:        %autorelease
Summary:        Disk Manager
License:        GPL-2.0-or-later
URL:            https://github.com/storaged-project/udisks
#!RemoteAsset:  sha256:0bf30151fe8d9d2fb59b57f6630739dfbbd16417dee69ec57d43b37335bd649a
Source0:        https://github.com/storaged-project/udisks/releases/download/udisks-%{version}/udisks-%{version}.tar.bz2
BuildSystem:    autotools

BuildOption(conf):  --enable-smart
BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-man
BuildOption(conf):  --enable-lvm2
BuildOption(conf):  --enable-btrfs
%if %{with doc}
BuildOption(conf):  --enable-gtk-doc
%else
BuildOption(conf):  --disable-gtk-doc
%endif
%if %{with iscsi}
BuildOption(conf):  --enable-iscsi
%else
BuildOption(conf):  --disable-iscsi
%endif
%if %{with lsm}
BuildOption(conf):  --enable-lsm
%else
BuildOption(conf):  --disable-lsm
%endif

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  python3dist(setuptools)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  polkit-devel >= 0.102
BuildRequires:  pkgconfig(libsystemd) >= 208
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libacl)
BuildRequires:  gettext-devel
BuildRequires:  libmount
BuildRequires:  libuuid
BuildRequires:  pkgconfig(blockdev)
%if %{with iscsi}
BuildRequires:  iscsi-initiator-utils-devel
%endif
%if %{with lsm}
BuildRequires:  libstoragemgmt-devel
BuildRequires:  libconfig-devel
%endif
%if %{with doc}
BuildRequires:  gtk-doc
%endif

Requires:       libblockdev
Requires:       dbus >= 1.4.0
Requires:       udev >= 208
Requires:       util-linux
Requires:       polkit >= 0.102
Requires:       lvm2
%if %{with iscsi}
Requires:       iscsi-initiator-utils
%endif
%if %{with lsm}
Requires:       libstoragemgmt
%endif

%description
The Udisks project provides a daemon, tools and libraries to access and
manipulate disks, storage devices and technologies.

%package        devel
Summary:        Development files for lib%{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for udisks2.

%install -a
find %{buildroot} -name '*.a' -delete

mkdir -p %{buildroot}%{_sysconfdir}/udisks2/modules.conf.d

# todo: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang %{name} --generate-subpackages

%post
%systemd_post udisks2.service
if [ -S /run/udev/control ]; then
    udevadm control --reload || :
    udevadm trigger || :
fi

%preun
%systemd_preun udisks2.service

%postun
%systemd_postun_with_restart udisks2.service

%files -f %{name}.lang
%license COPYING
%doc README.md AUTHORS NEWS HACKING
%dir %{_sysconfdir}/udisks2
%dir %{_sysconfdir}/udisks2/modules.conf.d
%config(noreplace) %{_sysconfdir}/udisks2/udisks2.conf
%config(noreplace) %{_sysconfdir}/udisks2/mount_options.conf.example
%{_datadir}/dbus-1/system.d/org.freedesktop.UDisks2.conf
%{_datadir}/bash-completion/completions/udisksctl
%{_datadir}/zsh/site-functions/_udisks2
%{_tmpfilesdir}/udisks2.conf
%{_unitdir}/udisks2.service
%{_udevrulesdir}/80-udisks2.rules
%{_sbindir}/umount.udisks2
%dir %{_libdir}/udisks2
%dir %{_libdir}/udisks2/modules
%dir %{_libexecdir}/udisks2
%{_libexecdir}/udisks2/udisksd
%{_bindir}/udisksctl
%{_datadir}/polkit-1/actions/org.freedesktop.UDisks2.policy
%{_datadir}/dbus-1/system-services/org.freedesktop.UDisks2.service
%attr(0700,root,root) %dir %{_localstatedir}/lib/udisks2
%{_datadir}/gtk-doc/html/udisks2
%{_libdir}/libudisks2.so.*
%{_libdir}/girepository-1.0/UDisks-2.0.typelib
%{_libdir}/udisks2/modules/libudisks2_lvm2.so
%{_datadir}/polkit-1/actions/org.freedesktop.UDisks2.lvm2.policy
%{_libdir}/pkgconfig/udisks2-lvm2.pc
%if %{with iscsi}
%{_libdir}/udisks2/modules/libudisks2_iscsi.so
%{_datadir}/polkit-1/actions/org.freedesktop.UDisks2.iscsi.policy
%{_libdir}/pkgconfig/udisks2-iscsi.pc
%endif
%{_libdir}/udisks2/modules/libudisks2_btrfs.so
%{_datadir}/polkit-1/actions/org.freedesktop.UDisks2.btrfs.policy
%{_libdir}/pkgconfig/udisks2-btrfs.pc
%if %{with lsm}
%{_libdir}/udisks2/modules/libudisks2_lsm.so
%{_mandir}/man5/udisks2_lsm.conf.*
%{_datadir}/polkit-1/actions/org.freedesktop.UDisks2.lsm.policy
%config(noreplace) %{_sysconfdir}/udisks2/modules.conf.d/udisks2_lsm.conf
%{_libdir}/pkgconfig/udisks2-lsm.pc
%endif

%files devel
%{_libdir}/libudisks2.so
%{_includedir}/udisks2/
%{_datadir}/gir-1.0/UDisks-2.0.gir
%{_libdir}/pkgconfig/udisks2.pc
%if %{with doc}
%doc %{_datadir}/gtk-doc/html/udisks2
%endif

%changelog
%autochangelog
