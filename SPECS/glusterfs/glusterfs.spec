# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           glusterfs
Version:        11.1
Release:        %autorelease
Summary:        Aggregating distributed file system
License:        GPL-2.0-only OR LGPL-3.0-or-later
URL:            https://www.gluster.org/
VCS:            git:https://github.com/gluster/glusterfs
#!RemoteAsset
Source:         https://download.gluster.org/pub/gluster/glusterfs/11/%{version}/glusterfs-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --without-tcmalloc
BuildOption(conf):  --disable-linux-io_uring
BuildOption(conf):  --with-mountutildir=%{_bindir}
BuildOption(conf):  --disable-static
BuildOption(conf):  --with-ipv6-default
BuildOption(install):  docdir=%{_docdir}/%{name}

BuildRequires:  pkgconfig(libacl)
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  pkgconfig(libaio)
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3
BuildRequires:  pkgconfig(readline)
BuildRequires:  rpcgen
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  pkgconfig(liburcu)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(uuid)

%description
GlusterFS is a clustered file-system capable of scaling to several
petabytes. It aggregates various storage bricks over Infiniband RDMA
or TCP/IP interconnect into one large parallel network file system.
GlusterFS is one of the most sophisticated file systems in terms of
features and extensibility. It borrows a powerful concept called
Translators from GNU Hurd kernel. Much of the code in GlusterFS is in
user space and easily manageable.

%package     -n python-gluster
Summary:        Python bindings for GlusterFS
Provides:       python3-gluster
%python_provide python3-gluster
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python-gluster
GlusterFS is a clustered file-system capable of scaling to several
petabytes.

%package        devel
Summary:        Development files for glusterfs
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(libacl)

%description    devel
GlusterFS is a clustered file-system capable of scaling to several
petabytes.

This package provides development files such as headers and library
links.

%conf -p
# Remove old python.m4 to use system default.
rm -f contrib/aclocal/python.m4
./autogen.sh

%install -a
mkdir -pv "%{buildroot}/%{_localstatedir}/log"/{glusterd,glusterfs,glusterfsd}
cp -av ChangeLog NEWS README.md "%{buildroot}/%{_docdir}/%{name}/"

chmod -v u-s "%{buildroot}/%{_bindir}/fusermount-glusterfs"
rm -fv "%{buildroot}/%{_bindir}/conf.py"
rm -f "%{buildroot}/etc/bash_completion.d/gluster.bash"
%fdupes %{buildroot}/%{_prefix}
%py3_shebang_fix .

%post
%systemd_post glusterd.service glustereventsd.service glusterfssharedstorage.service gluster-ta-volume.service

%preun
%systemd_preun glusterd.service glustereventsd.service glusterfssharedstorage.service gluster-ta-volume.service

%postun
%systemd_postun_with_restart glusterd.service glustereventsd.service glusterfssharedstorage.service gluster-ta-volume.service

%files
%license COPYING*
%dir %{_sysconfdir}/ganesha
%dir %{_sysconfdir}/glusterfs
%{_sysconfdir}/ganesha/*.sample
%config(noreplace) %{_sysconfdir}/glusterfs/eventsconfig.json
%config(noreplace) %{_sysconfdir}/glusterfs/g*lusterd.vol
%config(noreplace) %{_sysconfdir}/glusterfs/glusterfs-logrotate
%config %{_sysconfdir}/glusterfs/gluster-rsyslog*
%config %{_sysconfdir}/glusterfs/glusterfs-georep*
%config %{_sysconfdir}/glusterfs/group-*
%config %{_sysconfdir}/glusterfs/gsync*
%config %{_sysconfdir}/glusterfs/logger*
%config %{_sysconfdir}/glusterfs/thin*
%{_bindir}/fusermount-glusterfs
%{_libexecdir}/ganesha/
%{_libexecdir}/glusterfs/
%{_libdir}/glusterfs/
%{_bindir}/gluster*
%{_bindir}/gcron.py
%{_bindir}/gf_attach
%{_bindir}/gfind_missing_files
%{_bindir}/mount.glusterfs
%{_bindir}/snap_scheduler.py
%{_datadir}/glusterfs/
%{_mandir}/man*/*
%{_docdir}/glusterfs
%{_localstatedir}/lib/glusterd
%{_localstatedir}/log/glusterfs
%{_unitdir}/glusterd.service
%{_unitdir}/glustereventsd.service
%{_unitdir}/glusterfssharedstorage.service
%{_unitdir}/gluster-ta-volume.service
%{_prefix}/lib/ocf
# glusterfs runtime libs (libgfapi)
%{_libdir}/libgfapi.so.0*
# glusterfs runtime libs (libgfchangelog)
%{_libdir}/libgfchangelog.so.0*
# glusterfs runtime libs (libgfrpc)
%{_libdir}/libgfrpc.so.0*
# glusterfs runtime libs (libgfxdr)
%{_libdir}/libgfxdr.so.0*
# glusterfs runtime libs (libglusterfs)
%{_libdir}/libglusterfs.so.0*

%files -n python-gluster
%{python3_sitelib}/gluster/

%files devel
%{_includedir}/glusterfs/
%{_libdir}/libgfapi.so
%{_libdir}/libgfchangelog.so
%{_libdir}/libgfrpc.so
%{_libdir}/libgfxdr.so
%{_libdir}/libglusterfs.so
%{_libdir}/pkgconfig/glusterfs-api.pc
%{_libdir}/pkgconfig/libgfchangelog.pc

%changelog
%{?autochangelog}
