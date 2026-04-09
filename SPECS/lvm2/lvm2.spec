# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global device_mapper_version 1.02.209

# If we want to enable, change this to 1
%bcond lvmdbusd 0
%bcond lvmpolld 0
%bcond dmfilemapd 0

Name:           lvm2
Version:        2.03.35
# Do not reset Release to 1 unless both lvm2 and device-mapper
# versions are increased together.
Release:        %autorelease
Summary:        Userland logical volume management tools
License:        LicenseRef-DMIT
URL:            https://sourceware.org/lvm2
VCS:            git:https://gitlab.com/lvmteam/lvm2.git
#!RemoteAsset
Source0:        https://sourceware.org/pub/lvm2/releases/LVM2.%{version}.tgz
BuildSystem:    autotools

BuildOption(conf):  --with-default-dm-run-dir=%{_rundir}
BuildOption(conf):  --with-default-run-dir=%{_rundir}/lvm
BuildOption(conf):  --with-default-locking-dir=%{_rundir}/lock/lvm
BuildOption(conf):  --with-default-pid-dir=%{_rundir}
BuildOption(conf):  --with-udev-dir=%{_prefix}/lib/udev/rules.d
BuildOption(conf):  --with-usrlibdir=%{_libdir}
BuildOption(conf):  --enable-fsadm
BuildOption(conf):  --enable-write_install
BuildOption(conf):  --enable-pkgconfig
BuildOption(conf):  --enable-cmdlib
BuildOption(conf):  --enable-dmeventd
BuildOption(conf):  --enable-blkid_wiping
BuildOption(conf):  --enable-udev_sync
%if %{with lvmpolld}
BuildOption(conf):  --enable-lvmpolld
%endif
%if %{with lvmdbusd}
BuildOption(conf):  --enable-dbus-service
BuildOption(conf):  --enable-notify-dbus
%endif
%if %{with dmfilemapd}
BuildOption(conf):  --enable-dmfilemapd
%endif
BuildOption(conf):  --with-writecache=internal
BuildOption(conf):  --with-integrity=internal
BuildOption(conf):  --disable-silent-rules
BuildOption(conf):  --with-default-use-devices-file=1
BuildOption(conf):  --enable-readline

BuildRequires:  make
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libsepol)
BuildRequires:  util-linux-devel
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(libedit)
BuildRequires:  libaio
BuildRequires:  pkgconfig(libaio)
BuildRequires:  pkgconfig
BuildRequires:  kmod
BuildRequires:  pkgconfig(systemd)
BuildRequires:  systemd-units
BuildRequires:  pkgconfig(readline)
%if %{with lvmdbusd}
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-setuptools
BuildRequires:  python3-dbus
BuildRequires:  python3-pyudev
%endif

Requires:       %{name}-libs = %{version}-%{release}
Requires:       bash
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%description
LVM2 includes all of the support for handling read/write operations on
physical volumes (hard disks, RAID-Systems, magneto optical, etc.,
multiple devices (MD), see mdadm(8) or even loop devices, see
losetup(8)), creating volume groups (kind of virtual disks) from one
or more physical volumes and creating one or more logical volumes
(kind of logical partitions) in volume groups.

%package        devel
Summary:        Development libraries and headers
License:        LGPL-2.1-only
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       device-mapper-devel = %{device_mapper_version}-%{release}
Requires:       device-mapper-event-devel = %{device_mapper_version}-%{release}
Requires:       pkgconfig

%description    devel
This package contains files needed to develop applications that use
the lvm2 libraries.

%package        libs
Summary:        Shared libraries for lvm2
License:        LGPL-2.1-only
Requires:       device-mapper-event = %{device_mapper_version}-%{release}

%description    libs
This package contains shared lvm2 libraries for applications.

%if %{with lvmdbusd}
%package        dbusd
Summary:        LVM2 D-Bus daemon
License:        GPL-2.0-only
BuildArch:      noarch
Requires:       lvm2 >= %{version}-%{release}
Requires:       dbus
Requires:       python3-dbus
Requires:       python3-pyudev
Requires:       python3-gobject-base
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%description dbusd
Daemon for access to LVM2 functionality through a D-Bus interface.
%endif

%package     -n device-mapper
Summary:        Device mapper utility
Version:        %{device_mapper_version}
License:        GPL-2.0-only
URL:            https://www.sourceware.org/dm/
Requires:       device-mapper-libs = %{device_mapper_version}-%{release}
Requires:       util-linux
Requires:       systemd

%description -n device-mapper
This package contains the supporting userspace utility, dmsetup,
for the kernel device-mapper.

%package     -n device-mapper-devel
Summary:        Development libraries and headers for device-mapper
Version:        %{device_mapper_version}
License:        LGPL-2.1-only
Requires:       device-mapper = %{device_mapper_version}-%{release}
Requires:       pkgconfig

%description -n device-mapper-devel
This package contains files needed to develop applications that use
the device-mapper libraries.

%package     -n device-mapper-libs
Summary:        Device-mapper shared library
Version:        %{device_mapper_version}
License:        LGPL-2.1-only
Requires:       device-mapper = %{device_mapper_version}-%{release}

%description -n device-mapper-libs
This package contains the device-mapper shared library, libdevmapper.

%package     -n device-mapper-event
Summary:        Device-mapper event daemon
Version:        %{device_mapper_version}
Requires:       device-mapper = %{device_mapper_version}-%{release}
Requires:       device-mapper-event-libs = %{device_mapper_version}-%{release}
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%description -n device-mapper-event
This package contains the dmeventd daemon for monitoring the state
of device-mapper devices.

%package     -n device-mapper-event-libs
Summary:        Device-mapper event daemon shared library
Version:        %{device_mapper_version}
License:        LGPL-2.1-only

%description -n device-mapper-event-libs
This package contains the device-mapper event daemon shared library,
libdevmapper-event.

%package     -n device-mapper-event-devel
Summary:        Development libraries and headers for the device-mapper event daemon
Version:        %{device_mapper_version}
License:        LGPL-2.1-only
Requires:       device-mapper-event = %{device_mapper_version}-%{release}
Requires:       pkgconfig

%description -n device-mapper-event-devel
This package contains files needed to develop applications that use
the device-mapper event library.

%install -a
make install_system_dirs DESTDIR=%{buildroot}
make install_systemd_units DESTDIR=%{buildroot}
make install_systemd_generators DESTDIR=%{buildroot}
make install_tmpfiles_configuration DESTDIR=%{buildroot}

install -m 700 -d %{buildroot}%{_sharedstatedir}/lvm

%post
%systemd_post blk-availability.service lvm2-monitor.service
if [ "$1" = "1" ] ; then
    # FIXME: what to do with this? We do not want to start it in a container/chroot
    # enable and start lvm2-monitor.service on completely new installation only, not on upgrades
    systemctl enable lvm2-monitor.service
    systemctl start lvm2-monitor.service >/dev/null 2>&1 || :
fi

%if %{with lvmpolld}
%systemd_post lvm2-lvmpolld.socket
# lvm2-lvmpolld socket is always enabled and started and ready to serve if lvmpolld is used
# replace direct systemctl calls with systemd rpm macro once this is provided in the macro:
# http://cgit.freedesktop.org/systemd/systemd/commit/?id=57ab2eabb8f92fad5239c7d4492e9c6e23ee0678
systemctl enable lvm2-lvmpolld.socket
systemctl start lvm2-lvmpolld.socket >/dev/null 2>&1 || :
%endif

%if %{with lvmdbusd}
%post dbusd
%systemd_post lvm2-lvmdbusd.service
%endif

%post -n device-mapper-event
%systemd_post dm-event.socket
# dm-event.socket is always enabled and started and ready to serve if dmeventd is used
# replace direct systemctl calls with systemd rpm macro once this is provided in the macro:
# http://cgit.freedesktop.org/systemd/systemd/commit/?id=57ab2eabb8f92fad5239c7d4492e9c6e23ee0678
systemctl enable dm-event.socket
systemctl start dm-event.socket >/dev/null 2>&1 || :
if [ -e %{_default_pid_dir}/dmeventd.pid ]; then
    %{_sbindir}/dmeventd -R || echo "Failed to restart dmeventd daemon. Please, try manual restart."
fi

%preun
%systemd_preun blk-availability.service lvm2-monitor.service

%if %{with lvmpolld}
%systemd_preun lvm2-lvmpolld.service lvm2-lvmpolld.socket
%endif

%if %{with lvmdbusd}
%preun dbusd
%systemd_preun lvm2-lvmdbusd.service
%endif

%preun -n device-mapper-event
%systemd_preun dm-event.service dm-event.socket

%postun
%systemd_postun lvm2-monitor.service

%if %{with lvmpolld}
%systemd_postun_with_restart lvm2-lvmpolld.service
%endif

%if %{with lvmdbusd}
%postun dbusd
%systemd_postun lvm2-lvmdbusd.service
%endif

%files
%license COPYING COPYING.LIB
%doc README VERSION WHATS_NEW
%doc doc/lvm_fault_handling.txt
%{_sbindir}/fsadm
%{_sbindir}/lvm
%{_sbindir}/lvmconfig
%{_sbindir}/lvmdevices
%{_sbindir}/lvmdump
%{_sbindir}/lvmpersist
%if %{with lvmpolld}
%{_sbindir}/lvmpolld
%endif
%{_sbindir}/lvm_import_vdo
%{_sbindir}/lvchange
%{_sbindir}/lvconvert
%{_sbindir}/lvcreate
%{_sbindir}/lvdisplay
%{_sbindir}/lvextend
%{_sbindir}/lvmdiskscan
%{_sbindir}/lvmsadc
%{_sbindir}/lvmsar
%{_sbindir}/lvreduce
%{_sbindir}/lvremove
%{_sbindir}/lvrename
%{_sbindir}/lvresize
%{_sbindir}/lvs
%{_sbindir}/lvscan
%{_sbindir}/pvchange
%{_sbindir}/pvck
%{_sbindir}/pvcreate
%{_sbindir}/pvdisplay
%{_sbindir}/pvmove
%{_sbindir}/pvremove
%{_sbindir}/pvresize
%{_sbindir}/pvs
%{_sbindir}/pvscan
%{_sbindir}/vgcfgbackup
%{_sbindir}/vgcfgrestore
%{_sbindir}/vgchange
%{_sbindir}/vgck
%{_sbindir}/vgconvert
%{_sbindir}/vgcreate
%{_sbindir}/vgdisplay
%{_sbindir}/vgexport
%{_sbindir}/vgextend
%{_sbindir}/vgimport
%{_sbindir}/vgimportclone
%{_sbindir}/vgimportdevices
%{_sbindir}/vgmerge
%{_sbindir}/vgmknodes
%{_sbindir}/vgreduce
%{_sbindir}/vgremove
%{_sbindir}/vgrename
%{_sbindir}/vgs
%{_sbindir}/vgscan
%{_sbindir}/vgsplit
%attr(755, -, -) %{_libexecdir}/lvresize_fs_helper
%{_mandir}/man5/lvm.conf.5.gz
%{_mandir}/man7/lvmautoactivation.7.gz
%{_mandir}/man7/lvmcache.7.gz
%{_mandir}/man7/lvmraid.7.gz
%{_mandir}/man7/lvmreport.7.gz
%{_mandir}/man7/lvmthin.7.gz
%{_mandir}/man7/lvmvdo.7.gz
%{_mandir}/man7/lvmsystemid.7.gz
%{_mandir}/man8/fsadm.8.gz
%{_mandir}/man8/lvchange.8.gz
%{_mandir}/man8/lvconvert.8.gz
%{_mandir}/man8/lvcreate.8.gz
%{_mandir}/man8/lvdisplay.8.gz
%{_mandir}/man8/lvextend.8.gz
%{_mandir}/man8/lvm.8.gz
%{_mandir}/man8/lvm-config.8.gz
%{_mandir}/man8/lvm-dumpconfig.8.gz
%{_mandir}/man8/lvm-fullreport.8.gz
%{_mandir}/man8/lvmconfig.8.gz
%{_mandir}/man8/lvmdevices.8.gz
%{_mandir}/man8/lvmdiskscan.8.gz
%{_mandir}/man8/lvmdump.8.gz
%{_mandir}/man8/lvmpersist.8.gz
%{_mandir}/man8/lvmsadc.8.gz
%{_mandir}/man8/lvmsar.8.gz
%{_mandir}/man8/lvreduce.8.gz
%{_mandir}/man8/lvremove.8.gz
%{_mandir}/man8/lvrename.8.gz
%{_mandir}/man8/lvresize.8.gz
%{_mandir}/man8/lvs.8.gz
%{_mandir}/man8/lvscan.8.gz
%{_mandir}/man8/pvchange.8.gz
%{_mandir}/man8/pvck.8.gz
%{_mandir}/man8/pvcreate.8.gz
%{_mandir}/man8/pvdisplay.8.gz
%{_mandir}/man8/pvmove.8.gz
%{_mandir}/man8/pvremove.8.gz
%{_mandir}/man8/pvresize.8.gz
%{_mandir}/man8/pvs.8.gz
%{_mandir}/man8/pvscan.8.gz
%{_mandir}/man8/lvm_import_vdo.8.gz
%{_mandir}/man8/vgcfgbackup.8.gz
%{_mandir}/man8/vgcfgrestore.8.gz
%{_mandir}/man8/vgchange.8.gz
%{_mandir}/man8/vgck.8.gz
%{_mandir}/man8/vgconvert.8.gz
%{_mandir}/man8/vgcreate.8.gz
%{_mandir}/man8/vgdisplay.8.gz
%{_mandir}/man8/vgexport.8.gz
%{_mandir}/man8/vgextend.8.gz
%{_mandir}/man8/vgimport.8.gz
%{_mandir}/man8/vgimportclone.8.gz
%{_mandir}/man8/vgimportdevices.8.gz
%{_mandir}/man8/vgmerge.8.gz
%{_mandir}/man8/vgmknodes.8.gz
%{_mandir}/man8/vgreduce.8.gz
%{_mandir}/man8/vgremove.8.gz
%{_mandir}/man8/vgrename.8.gz
%{_mandir}/man8/vgs.8.gz
%{_mandir}/man8/vgscan.8.gz
%{_mandir}/man8/vgsplit.8.gz
# %{_udevdir} is not defined? - 251
%{_prefix}/lib/udev/rules.d/11-dm-lvm.rules
%{_prefix}/lib/udev/rules.d/69-dm-lvm.rules
%if %{with lvmpolld}
%{_mandir}/man8/lvmpolld.8.gz
%endif
%{_mandir}/man8/lvm-lvpoll.8.gz
%dir %{_sysconfdir}/lvm
%ghost %{_sysconfdir}/lvm/cache/.cache
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lvm/lvm.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lvm/lvmlocal.conf
%dir %{_sysconfdir}/lvm/profile
%{_sysconfdir}/lvm/profile/command_profile_template.profile
%{_sysconfdir}/lvm/profile/metadata_profile_template.profile
%{_sysconfdir}/lvm/profile/thin-generic.profile
%{_sysconfdir}/lvm/profile/thin-performance.profile
%{_sysconfdir}/lvm/profile/cache-mq.profile
%{_sysconfdir}/lvm/profile/cache-smq.profile
%{_sysconfdir}/lvm/profile/lvmdbusd.profile
%{_sysconfdir}/lvm/profile/vdo-small.profile
%dir %{_sysconfdir}/lvm/backup
%dir %{_sysconfdir}/lvm/cache
%dir %{_sysconfdir}/lvm/archive
%dir %{_sysconfdir}/lvm/devices
%dir %{_rundir}/lock/lvm
%dir %{_rundir}/lvm
%{_tmpfilesdir}/%{name}.conf
%{_unitdir}/blk-availability.service
%{_unitdir}/lvm2-monitor.service
%if %{with lvmpolld}
%{_unitdir}/lvm2-lvmpolld.socket
%{_unitdir}/lvm2-lvmpolld.service
%endif
%{_unitdir}/lvm-devices-import.service
%{_unitdir}/lvm-devices-import.path
%dir %{_sharedstatedir}/lvm

%files devel
%{_libdir}/liblvm2cmd.so
%{_libdir}/libdevmapper-event-lvm2.so
%{_includedir}/lvm2cmd.h

%files libs
%license COPYING.LIB
%{_libdir}/liblvm2cmd.so.*
%{_libdir}/libdevmapper-event-lvm2.so.*
%dir %{_libdir}/device-mapper
%{_libdir}/device-mapper/libdevmapper-event-lvm2mirror.so
%{_libdir}/device-mapper/libdevmapper-event-lvm2snapshot.so
%{_libdir}/device-mapper/libdevmapper-event-lvm2raid.so
%{_libdir}/libdevmapper-event-lvm2mirror.so
%{_libdir}/libdevmapper-event-lvm2snapshot.so
%{_libdir}/libdevmapper-event-lvm2raid.so
%{_libdir}/libdevmapper-event-lvm2thin.so
%{_libdir}/device-mapper/libdevmapper-event-lvm2thin.so
%{_libdir}/libdevmapper-event-lvm2vdo.so
%{_libdir}/device-mapper/libdevmapper-event-lvm2vdo.so

%if %{with lvmdbusd}
%files dbusd
%{_sbindir}/lvmdbusd
%{_sysconfdir}/dbus-1/system.d/com.redhat.lvmdbus1.conf
%{_datadir}/dbus-1/system-services/com.redhat.lvmdbus1.service
%{_mandir}/man8/lvmdbusd.8.gz
%{_unitdir}/lvm2-lvmdbusd.service
%{python3_sitelib}/lvmdbusd
%endif

%files -n device-mapper
%license COPYING COPYING.LIB
%doc WHATS_NEW_DM VERSION_DM README
%doc udev/12-dm-permissions.rules
%{_sbindir}/dmsetup
%{_sbindir}/blkdeactivate
%{_sbindir}/dmstats
%{_mandir}/man8/dmsetup.8.gz
%{_mandir}/man8/dmstats.8.gz
%{_mandir}/man8/blkdeactivate.8.gz
%if %{with dmfilemapd}
%{_sbindir}/dmfilemapd
%{_mandir}/man8/dmfilemapd.8.gz
%endif
%{_prefix}/lib/udev/rules.d/10-dm.rules
%{_prefix}/lib/udev/rules.d/13-dm-disk.rules
%{_prefix}/lib/udev/rules.d/95-dm-notify.rules

%files -n device-mapper-devel
%{_libdir}/libdevmapper.so
%{_includedir}/libdevmapper.h
%{_libdir}/pkgconfig/devmapper.pc

%files -n device-mapper-libs
%license COPYING COPYING.LIB
%{_libdir}/libdevmapper.so.*

%files -n device-mapper-event
%{_sbindir}/dmeventd
%{_mandir}/man8/dmeventd.8.gz
%{_unitdir}/dm-event.socket
%{_unitdir}/dm-event.service

%files -n device-mapper-event-libs
%license COPYING.LIB
%{_libdir}/libdevmapper-event.so.*

%files -n device-mapper-event-devel
%{_libdir}/libdevmapper-event.so
%{_includedir}/libdevmapper-event.h
%{_libdir}/pkgconfig/devmapper-event.pc

%changelog
%autochangelog
