# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           nfs-utils
Version:        2.8.4
Release:        %autorelease
Summary:        Support Utilities for Kernel nfsd
License:        GPL-2.0-or-later
URL:            https://kernel.org/pub/linux/utils/nfs-utils/
VCS:            git:git://git.linux-nfs.org/projects/steved/nfs-utils.git
#!RemoteAsset
Source0:        https://kernel.org/pub/linux/utils/nfs-utils/%{version}/nfs-utils-%{version}.tar.xz
Source1:        sysconfig.nfs
Source2:        idmapd.conf
Source3:        statd-user.sysusers
Source4:        nfs.conf
Source5:        nfs-kernel-server.tmpfiles
BuildSystem:    autotools

BuildOption(conf):  --with-systemd
BuildOption(conf):  --enable-nfsv4
BuildOption(conf):  --enable-gss
BuildOption(conf):  --enable-svcgss
BuildOption(conf):  --enable-ipv6
BuildOption(conf):  --enable-nfsdcltrack
BuildOption(conf):  --enable-mount
BuildOption(conf):  --enable-libmount-mount
BuildOption(conf):  --enable-junction
BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-sbin-override
BuildOption(conf):  --with-pluginpath=%{_libdir}/libnfsidmap
BuildOption(conf):  --enable-mountconfig

BuildRequires:  e2fsprogs
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  glibc-devel
BuildRequires:  rpcgen
BuildRequires:  pkgconfig(kdb)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libkeyutils)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(mount)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(devmapper)
BuildRequires:  autoconf
BuildRequires:  automake
%{?systemd_ordering}

%description
This package contains the NFS utilities. This is a metapackage that requires
the NFS kernel server utilities.

%package     -n nfs-client
Summary:        Support Utilities for NFS Client
Requires:       keyutils
Requires:       rpcbind
Requires(pre):  systemd-sysusers

%description -n nfs-client
This package contains common NFS utilities which are needed for an NFS client.

%package     -n nfs-kernel-server
Summary:        Support Utilities for Kernel NFS Server
Requires:       nfs-client = %{version}-%{release}
Requires:       rpcbind
Requires:       (kmod(nfsd.ko) if kernel)
Provides:       nfs-utils = %{version}-%{release}

%description -n nfs-kernel-server
This package contains support for the kernel-based NFS server.

%package     -n nfsidmap
Summary:        NFSv4 ID Mapping Library

%description -n nfsidmap
This library provides NFSv4 user/group name to ID mapping functionality.

%package     -n nfsidmap-devel
Summary:        Development files for the NFSv4 ID Mapping Library
Requires:       nfsidmap = %{version}-%{release}

%description -n nfsidmap-devel
This package contains header files for the NFSv4 ID Mapping Library.

%conf -p
autoreconf -fiv

%install -a
install -d %{buildroot}%{_sysusersdir}
install -m 644 %{SOURCE3} %{buildroot}%{_sysusersdir}/statd-user.conf

install -D -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/nfs.conf
install -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/nfs
mkdir -p -m 755 %{buildroot}%{_sysconfdir}/nfs.conf.d
install -D -m 644 %{SOURCE5} %{buildroot}%{_prefix}/lib/tmpfiles.d/nfs-kernel-server.conf
install -D -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/idmapd.conf
mkdir -p -m 755 %{buildroot}%{_sysconfdir}/idmapd.conf.d
mkdir -p -m 755 %{buildroot}%{_localstatedir}/lib/nfs/rpc_pipefs
mkdir -p -m 755 %{buildroot}%{_localstatedir}/lib/nfs/v4recovery
mkdir -p -m 755 %{buildroot}%{_localstatedir}/lib/nfs/sm
mkdir -p -m 755 %{buildroot}%{_localstatedir}/lib/nfs/sm.bak
touch %{buildroot}%{_localstatedir}/lib/nfs/state
mkdir -p -m 755 %{buildroot}%{_sysconfdir}/nfsmount.conf.d
chmod 644 `grep -l -r '^#!/usr/bin/python' %{buildroot}%{_sbindir}` || :

%pre -n nfs-client
%sysusers_create_package statd %{SOURCE3}

%post -n nfs-client
chown root:root %{_localstatedir}/lib/nfs > /dev/null 2>&1 || :
for i in sm sm.bak; do
    p=%{_localstatedir}/lib/nfs/$i
    if [ -d "$p" ] && [ -n "`chown 2> /dev/null -c --from root statd:statd $p`" ]; then
	chown -R statd:statd $p > /dev/null 2>&1 || :
    fi
done
[ -d /run/nfs ] || mkdir /run/nfs
if [ -f %{_localstatedir}/lock/subsys/nfs-rpc.idmapd ]; then
	mv %{_localstatedir}/lock/subsys/nfs-rpc.idmapd /run/nfs
fi
if [ -f %{_localstatedir}/lock/subsys/nfsserver-rpc.idmapd ]; then
	mv %{_localstatedir}/lock/subsys/nfsserver-rpc.idmapd /run/nfs
fi
%systemd_post auth-rpcgss-module.service nfs-idmapd.service nfs-blkmap.service rpc-statd-notify.service rpc-gssd.service rpc-statd.service rpc-svcgssd.service

%preun -n nfs-client
%systemd_preun auth-rpcgss-module.service nfs-idmapd.service nfs-blkmap.service rpc-statd-notify.service rpc-gssd.service rpc-statd.service rpc-svcgssd.service

%postun -n nfs-client
%systemd_postun auth-rpcgss-module.service nfs-idmapd.service nfs-blkmap.service rpc-statd-notify.service rpc-gssd.service rpc-statd.service rpc-svcgssd.service

%preun -n nfs-kernel-server
%systemd_preun nfs-svcgssd.service nfs-mountd.service nfs-server.service

%post -n nfs-kernel-server
[ -d /run/nfs ] || mkdir /run/nfs
if [ -f %{_localstatedir}/lock/subsys/nfs-rpc.idmapd ]; then
	mv %{_localstatedir}/lock/subsys/nfs-rpc.idmapd /run/nfs
fi
if [ -f %{_localstatedir}/lock/subsys/nfsserver-rpc.idmapd ]; then
	mv %{_localstatedir}/lock/subsys/nfsserver-rpc.idmapd /run/nfs
fi
%systemd_post nfs-mountd.service nfs-server.service nfsdcld.service
%tmpfiles_create_package nfs-kernel-server %{SOURCE5}

%postun -n nfs-kernel-server
%systemd_postun nfs-mountd.service nfs-server.service nfsdcld.service

%files
%license COPYING
%doc README

%files -n nfs-client
%license COPYING
%config(noreplace) %{_sysconfdir}/idmapd.conf
%dir %{_sysconfdir}/idmapd.conf.d
%dir %{_sysconfdir}/nfsmount.conf.d
%config(noreplace) %{_sysconfdir}/nfs.conf
%config(noreplace) %{_sysconfdir}/sysconfig/nfs
%dir %{_sysconfdir}/nfs.conf.d
%doc utils/mount/nfsmount.conf
%verify(not mode) %attr(0755,root,root) %{_sbindir}/mount.nfs
%{_sbindir}/mount.nfs4
%{_sbindir}/umount.nfs
%{_sbindir}/umount.nfs4
%attr(0755,root,root) %{_sbindir}/mountstats
%attr(0755,root,root) %{_sbindir}/nfsiostat
%{_sbindir}/nfsdcld
%{_sbindir}/nfsidmap
%{_sbindir}/nfsstat
%{_sbindir}/rpc.gssd
%{_sbindir}/rpc.idmapd
%{_sbindir}/rpc.statd
%{_sbindir}/rpcctl
%{_sbindir}/rpcdebug
%{_sbindir}/showmount
%{_sbindir}/sm-notify
%{_sbindir}/start-statd
%{_sbindir}/blkmapd
%{_sbindir}/rpc.svcgssd
%{_sbindir}/nfsconf
%{_udevrulesdir}/60-nfs.rules
%{_udevrulesdir}/99-nfs.rules
%{_unitdir}/auth-rpcgss-module.service
%{_unitdir}/fsidd.service
%{_unitdir}/nfs-blkmap.service
%{_unitdir}/nfs-client.target
%{_unitdir}/nfs-idmapd.service
%{_unitdir}/nfs-utils.service
%{_unitdir}/nfsdcld.service
%{_unitdir}/rpc-gssd.service
%{_unitdir}/rpc_pipefs.target
%{_unitdir}/rpc-statd-notify.service
%{_unitdir}/rpc-statd.service
%{_unitdir}/rpc-svcgssd.service
%{_unitdir}/var-lib-nfs-rpc_pipefs.mount
%dir %{_systemdgeneratordir}
%{_systemdgeneratordir}/nfs-server-generator
%{_systemdgeneratordir}/rpc-pipefs-generator
%{_systemdgeneratordir}/nfsroot-generator
%{_mandir}/man5/idmapd.conf.5*
%{_mandir}/man5/nfs.5*
%{_mandir}/man5/nfs.conf.5*
%{_mandir}/man5/nfsmount.conf.5*
%{_mandir}/man5/nfsrahead.5*
%{_mandir}/man7/nfs.systemd.7*
%{_mandir}/man8/blkmapd.8*
%{_mandir}/man8/gssd.8*
%{_mandir}/man8/idmapd.8*
%{_mandir}/man8/mount.nfs.8*
%{_mandir}/man8/mountstats.8*
%{_mandir}/man8/nfsconf.8*
%{_mandir}/man8/nfsdcld.8*
%{_mandir}/man8/nfsdclddb.8*
%{_mandir}/man8/nfsdclnts.8*
%{_mandir}/man8/nfsidmap.8*
%{_mandir}/man8/nfsiostat.8*
%{_mandir}/man8/nfsstat.8*
%{_mandir}/man8/rpc.gssd.8*
%{_mandir}/man8/rpc.idmapd.8*
%{_mandir}/man8/rpc.sm-notify.8*
%{_mandir}/man8/rpc.statd.8*
%{_mandir}/man8/rpc.svcgssd.8*
%{_mandir}/man8/rpcctl.8*
%{_mandir}/man8/rpcdebug.8*
%{_mandir}/man8/showmount.8*
%{_mandir}/man8/sm-notify.8*
%{_mandir}/man8/statd.8*
%{_mandir}/man8/svcgssd.8*
%{_mandir}/man8/umount.nfs.8*
%{_sysusersdir}/statd-user.conf
%dir %{_localstatedir}/lib/nfs
%dir %{_localstatedir}/lib/nfs/rpc_pipefs
%dir %{_localstatedir}/lib/nfs/v4recovery
%attr(0700,statd,statd) %dir %{_localstatedir}/lib/nfs/sm
%attr(0700,statd,statd) %dir %{_localstatedir}/lib/nfs/sm.bak
%ghost %{_localstatedir}/lib/nfs/state
%{_libexecdir}/nfsrahead

%files -n nfs-kernel-server
%{_unitdir}/nfs-mountd.service
%{_unitdir}/nfs-server.service
%{_unitdir}/proc-fs-nfsd.mount
%{_prefix}/lib/tmpfiles.d/nfs-kernel-server.conf
%{_sbindir}/exportfs
%{_sbindir}/fsidd
%{_sbindir}/rpc.mountd
%{_sbindir}/rpc.nfsd
%{_sbindir}/nfsdcltrack
%{_sbindir}/nfsdctl
%{_sbindir}/nfsref
%attr(0755,root,root) %{_sbindir}/nfsdclddb
%attr(0755,root,root) %{_sbindir}/nfsdclnts
%{_mandir}/man5/exports.5*
%{_mandir}/man7/nfsd.7*
%{_mandir}/man8/exportfs.8*
%{_mandir}/man8/mountd.8*
%{_mandir}/man8/nfsd.8*
%{_mandir}/man8/nfsref.8*
%{_mandir}/man8/rpc.mountd.8*
%{_mandir}/man8/rpc.nfsd.8*
%{_mandir}/man8/nfsdctl.8*
%{_mandir}/man8/nfsdcltrack.8*
%config(noreplace) %{_localstatedir}/lib/nfs/etab
%config(noreplace) %{_localstatedir}/lib/nfs/rmtab

%files -n nfsidmap
%{_libdir}/libnfsidmap.so.1*
%{_libdir}/libnfsidmap/

%files -n nfsidmap-devel
%{_libdir}/libnfsidmap.so
%{_includedir}/nfsidmap.h
%{_includedir}/nfsidmap_plugin.h
%{_libdir}/pkgconfig/libnfsidmap.pc
%doc support/nfsidmap/README
%{_mandir}/man3/*

%changelog
%autochangelog
