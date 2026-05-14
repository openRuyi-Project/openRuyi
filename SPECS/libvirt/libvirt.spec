# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global qemu_user qemu
%global qemu_group qemu
%global qemu_moddir %{_libdir}/qemu
%global qemu_datadir %{_datadir}/qemu
%global tls_priority @LIBVIRT,SYSTEM
%global firewall_backend_priority nftables,iptables

Name:           libvirt
Version:        12.2.0
Release:        %autorelease
Summary:        Library providing a simple virtualization API
License:        GPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND OFL-1.1
URL:            https://libvirt.org
VCS:            git:https://gitlab.com/libvirt/libvirt.git
#!RemoteAsset:  sha256:ac93cd0da743a6c231911fb549399b415102ecfee775329bebbf61ed843b9786
Source0:        https://libvirt.org/sources/%{name}-%{version}.tar.xz
BuildSystem:    meson

BuildOption(conf):  -Dsystem=true
BuildOption(conf):  -Dno_git=true
BuildOption(conf):  -Dapparmor=disabled
BuildOption(conf):  -Dsecdriver_apparmor=disabled
BuildOption(conf):  -Dapparmor_profiles=disabled
BuildOption(conf):  -Drunstatedir=%{_rundir}
BuildOption(conf):  -Dinitconfdir=%{_sysconfdir}/sysconfig
BuildOption(conf):  -Dunitdir=%{_unitdir}
BuildOption(conf):  -Dsysusersdir=%{_sysusersdir}
BuildOption(conf):  -Ddriver_bhyve=disabled
BuildOption(conf):  -Ddriver_libxl=disabled
BuildOption(conf):  -Ddriver_esx=disabled
BuildOption(conf):  -Ddriver_hyperv=disabled
BuildOption(conf):  -Ddriver_vmware=disabled
BuildOption(conf):  -Ddriver_openvz=disabled
BuildOption(conf):  -Ddriver_vbox=disabled
BuildOption(conf):  -Ddriver_vz=disabled
BuildOption(conf):  -Ddriver_ch=disabled
BuildOption(conf):  -Dremote_default_mode=direct
BuildOption(conf):  -Dnetcf=disabled
BuildOption(conf):  -Dstorage_vstorage=disabled
BuildOption(conf):  -Dstorage_zfs=disabled
BuildOption(conf):  -Dnumad=disabled
BuildOption(conf):  -Dselinux_mount=/sys/fs/selinux
BuildOption(conf):  -Dsanlock=disabled
BuildOption(conf):  -Dnbdkit=disabled
BuildOption(conf):  -Dnbdkit_config_default=disabled
BuildOption(conf):  -Dopenwsman=disabled
BuildOption(conf):  -Dpm_utils=disabled
BuildOption(conf):  -Dwireshark_dissector=disabled
BuildOption(conf):  -Dqemu_user=%{qemu_user}
BuildOption(conf):  -Dqemu_group=%{qemu_group}
BuildOption(conf):  -Dqemu_moddir=%{qemu_moddir}
BuildOption(conf):  -Dqemu_datadir=%{qemu_datadir}
BuildOption(conf):  -Dtls_priority=%{tls_priority}
BuildOption(conf):  -Dinit_script=systemd
BuildOption(conf):  -Dfirewall_backend_priority=%{firewall_backend_priority}
BuildOption(conf):  -Dtests=enabled
BuildOption(conf):  -Dexpensive_tests=enabled
BuildOption(conf):  -Drpath=disabled

BuildRequires:  augeas
BuildRequires:  firewall-macros
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  perl
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(docutils)
BuildRequires:  systemd-rpm-macros
BuildRequires:  systemtap-sdt-devel
BuildRequires:  systemtap-sdt-dtrace
BuildRequires:  qemu-tools
BuildRequires:  ceph-devel
BuildRequires:  gawk
BuildRequires:  libxslt
BuildRequires:  pkgconfig(audit)
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(devmapper)
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.66
BuildRequires:  pkgconfig(glib-2.0) >= 2.66
BuildRequires:  pkgconfig(glusterfs-api) >= 3.4.1
BuildRequires:  pkgconfig(gobject-2.0) >= 2.66
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libacl)
BuildRequires:  pkgconfig(libattr)
BuildRequires:  pkgconfig(libcap-ng)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libiscsi)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libnl-route-3.0)
BuildRequires:  pkgconfig(libparted)
BuildRequires:  pkgconfig(libpcap)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libssh)
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  pkgconfig(libtasn1)
BuildRequires:  pkgconfig(libsasl2)
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(numa)
BuildRequires:  pkgconfig(pciaccess)
BuildRequires:  pkgconfig(readline)

Requires:       %{name}-client%{_isa} = %{version}-%{release}
Requires:       %{name}-daemon%{_isa} = %{version}-%{release}

%description
Libvirt is a C toolkit to interact with the virtualization capabilities of
recent versions of Linux and other operating systems. The main package pulls in
the client utilities and daemon components.

%package        client
Summary:        Client side utilities of the libvirt library

%description    client
The client binaries needed to access the virtualization capabilities of recent
versions of Linux and other operating systems.

%package        daemon
Summary:        Server side daemon and drivers for libvirt
Requires:       %{name}-daemon-driver-lxc%{_isa} = %{version}-%{release}
Requires:       %{name}-daemon-driver-others%{_isa} = %{version}-%{release}
Requires:       %{name}-daemon-driver-qemu%{_isa} = %{version}-%{release}
Requires:       %{name}-daemon-driver-storage-fs%{_isa} = %{version}-%{release}
Requires:       %{name}-daemon-driver-storage-lvm%{_isa} = %{version}-%{release}
Requires:       dbus
Requires:       gettext
Requires:       iproute2
Requires:       kmod
Requires:       polkit

%description    daemon
The daemon binaries and drivers needed to expose virtualization capabilities
through libvirt. This package pulls in the supported daemon driver packages.

%package        daemon-driver-qemu
Summary:        QEMU driver for libvirt
Requires:       %{name}-client%{_isa} = %{version}-%{release}
Requires:       bzip2
Requires:       gzip
Requires:       lzop
Requires:       qemu-system
Requires:       qemu-tools
Requires:       swtpm
Requires:       systemd-container
Requires:       xz
Requires:       zstd

%description    daemon-driver-qemu
The QEMU driver for the libvirt daemon.

%package        daemon-driver-lxc
Summary:        LXC driver for libvirt
Requires:       %{name}-client%{_isa} = %{version}-%{release}
Requires:       systemd-container

%description    daemon-driver-lxc
The Linux Container driver for the libvirt daemon.

%package        daemon-driver-storage-fs
Summary:        Filesystem storage driver for libvirt
Requires:       %{name}-client%{_isa} = %{version}-%{release}
Requires:       qemu-tools
Requires:       util-linux

%description    daemon-driver-storage-fs
The filesystem storage driver and common storage daemon for libvirt.

%package        daemon-driver-storage-lvm
Summary:        LVM storage driver for libvirt
Requires:       %{name}-daemon-driver-storage-fs%{_isa} = %{version}-%{release}
Requires:       lvm2

%description    daemon-driver-storage-lvm
The LVM storage backend for libvirt.

%package        daemon-driver-others
Summary:        Additional daemon drivers for libvirt
Requires:       %{name}-client%{_isa} = %{version}-%{release}
Requires:       device-mapper
Requires:       dnsmasq
Requires:       glusterfs
Requires:       open-iscsi
Requires:       parted

%description    daemon-driver-others
Additional libvirt daemon drivers and daemon support files that are not split
into dedicated driver packages yet.

%package        devel
Summary:        Development files for libvirt
Requires:       %{name}-client%{_isa} = %{version}-%{release}

%description    devel
This package contains the header files and pkg-config files needed to develop
applications using libvirt.

%install -a
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS.rst CONTRIBUTING.rst NEWS.rst README.rst
%doc %{_docdir}/%{name}/examples/
%doc %{_docdir}/%{name}/html/
%license COPYING COPYING.LESSER

%files client
%{_bindir}/virsh
%{_bindir}/virt-admin
%{_bindir}/virt-host-validate
%{_bindir}/virt-login-shell
%{_bindir}/virt-pki-validate
%{_bindir}/virt-xml-validate
%{_libexecdir}/virt-login-shell-helper
%{_libdir}/libvirt*.so.*
%{_datadir}/bash-completion/completions/virsh
%{_mandir}/man1/virsh.1*
%{_mandir}/man1/virt-admin.1*
%{_mandir}/man1/virt-host-validate.1*
%{_mandir}/man1/virt-login-shell.1*
%{_mandir}/man1/virt-pki-query-dn.1*
%{_mandir}/man1/virt-pki-validate.1*
%{_mandir}/man1/virt-xml-validate.1*
%{_mandir}/man7/virkey*.7*
%config(noreplace) %{_sysconfdir}/ssh/ssh_config.d/*libvirt*.conf
%{_sysconfdir}/libvirt/libvirt.conf
%{_sysconfdir}/libvirt/virt-login-shell.conf

%files daemon
%{_sbindir}/libvirtd
%{_datadir}/bash-completion/completions/virt-admin
%{_datadir}/libvirt/
%exclude %{_datadir}/libvirt/api/
%exclude %{_datadir}/libvirt/api/*
%{_datadir}/polkit-1/actions/*libvirt*.policy
%{_datadir}/polkit-1/rules.d/*libvirt*.rules
%{_unitdir}/libvirtd.service
%{_unitdir}/libvirtd.socket
%{_unitdir}/libvirtd-ro.socket
%{_unitdir}/libvirtd-admin.socket
%{_unitdir}/*virt*.target
%{_prefix}/lib/sysctl.d/*libvirt*.conf
%{_sysusersdir}/*virt*.conf
%exclude %{_sysusersdir}/libvirt-qemu.conf
%{_mandir}/man8/libvirtd.8*

%files daemon-driver-qemu
%config(noreplace) %{_sysconfdir}/libvirt/virtqemud.conf
%config(noreplace) %{_sysconfdir}/libvirt/qemu.conf
%config(noreplace) %{_sysconfdir}/libvirt/qemu-lockd.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/libvirtd.qemu
%{_bindir}/virt-qemu-run
%{_bindir}/virt-qemu-qmp-proxy
%{_bindir}/virt-qemu-sev-validate
%{_sbindir}/virtqemud
%{_datadir}/augeas/lenses/libvirtd_qemu.aug
%{_datadir}/augeas/lenses/virtqemud.aug
%{_datadir}/augeas/lenses/tests/test_libvirtd_qemu.aug
%{_datadir}/augeas/lenses/tests/test_virtqemud.aug
%{_libdir}/libvirt/connection-driver/libvirt_driver_qemu.so
%{_mandir}/man1/virt-qemu-run.1*
%{_mandir}/man1/virt-qemu-qmp-proxy.1*
%{_mandir}/man1/virt-qemu-sev-validate.1*
%{_mandir}/man8/virtqemud.8*
%{_unitdir}/virtqemud.service
%{_unitdir}/virtqemud.socket
%{_unitdir}/virtqemud-ro.socket
%{_unitdir}/virtqemud-admin.socket
%{_sysusersdir}/libvirt-qemu.conf
%dir %attr(0700, root, root) %{_sysconfdir}/libvirt/qemu/
%dir %attr(0700, root, root) %{_sysconfdir}/libvirt/qemu/autostart/
%dir %attr(0751, %{qemu_user}, %{qemu_group}) %{_localstatedir}/lib/libvirt/qemu/
%dir %attr(0751, %{qemu_user}, %{qemu_group}) %{_localstatedir}/lib/libvirt/qemu/checkpoint/
%dir %attr(0751, %{qemu_user}, %{qemu_group}) %{_localstatedir}/lib/libvirt/qemu/dump/
%dir %attr(0751, %{qemu_user}, %{qemu_group}) %{_localstatedir}/lib/libvirt/qemu/nvram/
%dir %attr(0751, %{qemu_user}, %{qemu_group}) %{_localstatedir}/lib/libvirt/qemu/ram/
%dir %attr(0751, %{qemu_user}, %{qemu_group}) %{_localstatedir}/lib/libvirt/qemu/save/
%dir %attr(0751, %{qemu_user}, %{qemu_group}) %{_localstatedir}/lib/libvirt/qemu/snapshot/
%dir %attr(0751, %{qemu_user}, %{qemu_group}) %{_localstatedir}/lib/libvirt/qemu/varstore/
%dir %attr(0750, root, root) %{_localstatedir}/cache/libvirt/qemu/
%dir %attr(0700, root, root) %{_localstatedir}/log/libvirt/qemu/
%ghost %dir %attr(0755, %{qemu_user}, %{qemu_group}) %{_rundir}/libvirt/qemu/
%ghost %dir %attr(0770, %{qemu_user}, %{qemu_group}) %{_rundir}/libvirt/qemu/dbus/
%ghost %dir %attr(0755, %{qemu_user}, %{qemu_group}) %{_rundir}/libvirt/qemu/passt/
%ghost %dir %attr(0755, %{qemu_user}, %{qemu_group}) %{_rundir}/libvirt/qemu/slirp/
%ghost %dir %attr(0770, %{qemu_user}, %{qemu_group}) %{_rundir}/libvirt/qemu/swtpm/

%files daemon-driver-lxc
%config(noreplace) %{_sysconfdir}/libvirt/virtlxcd.conf
%config(noreplace) %{_sysconfdir}/libvirt/lxc.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/libvirtd.lxc
%{_sbindir}/virtlxcd
%{_libexecdir}/libvirt_lxc
%{_datadir}/augeas/lenses/libvirtd_lxc.aug
%{_datadir}/augeas/lenses/virtlxcd.aug
%{_datadir}/augeas/lenses/tests/test_libvirtd_lxc.aug
%{_datadir}/augeas/lenses/tests/test_virtlxcd.aug
%{_libdir}/libvirt/connection-driver/libvirt_driver_lxc.so
%{_mandir}/man8/virtlxcd.8*
%{_unitdir}/virtlxcd.service
%{_unitdir}/virtlxcd.socket
%{_unitdir}/virtlxcd-ro.socket
%{_unitdir}/virtlxcd-admin.socket
%dir %attr(0700, root, root) %{_sysconfdir}/libvirt/lxc/
%dir %attr(0700, root, root) %{_sysconfdir}/libvirt/lxc/autostart/
%dir %attr(0700, root, root) %{_localstatedir}/log/libvirt/lxc/
%dir %attr(0700, root, root) %{_localstatedir}/lib/libvirt/lxc/
%ghost %dir %{_rundir}/libvirt/lxc/

%files daemon-driver-storage-fs
%config(noreplace) %{_sysconfdir}/libvirt/virtstoraged.conf
%{_sbindir}/virtstoraged
%{_libexecdir}/libvirt_parthelper
%{_datadir}/augeas/lenses/virtstoraged.aug
%{_datadir}/augeas/lenses/tests/test_virtstoraged.aug
%{_libdir}/libvirt/connection-driver/libvirt_driver_storage.so
%{_libdir}/libvirt/storage-backend/libvirt_storage_backend_fs.so
%{_mandir}/man8/virtstoraged.8*
%{_unitdir}/virtstoraged.service
%{_unitdir}/virtstoraged.socket
%{_unitdir}/virtstoraged-ro.socket
%{_unitdir}/virtstoraged-admin.socket
%dir %attr(0700, root, root) %{_sysconfdir}/libvirt/storage/
%dir %attr(0700, root, root) %{_sysconfdir}/libvirt/storage/autostart/
%ghost %dir %{_rundir}/libvirt/storage/

%files daemon-driver-storage-lvm
%{_libdir}/libvirt/storage-backend/libvirt_storage_backend_logical.so

%files daemon-driver-others
%config(noreplace) %{_sysconfdir}/sasl2/libvirt.conf
%{_sbindir}/virt*
%exclude %{_sbindir}/virtqemud
%exclude %{_sbindir}/virtlxcd
%exclude %{_sbindir}/virtstoraged
%{_libexecdir}/libvirt*
%exclude %{_libexecdir}/libvirt_lxc
%exclude %{_libexecdir}/libvirt_parthelper
%{_libdir}/libvirt/connection-driver/
%exclude %{_libdir}/libvirt/connection-driver/libvirt_driver_qemu.so
%exclude %{_libdir}/libvirt/connection-driver/libvirt_driver_lxc.so
%exclude %{_libdir}/libvirt/connection-driver/libvirt_driver_storage.so
%{_libdir}/libvirt/storage-backend/
%exclude %{_libdir}/libvirt/storage-backend/libvirt_storage_backend_fs.so
%exclude %{_libdir}/libvirt/storage-backend/libvirt_storage_backend_logical.so
%{_libdir}/libvirt/storage-file/
%{_libdir}/libvirt/lock-driver/
%{_libdir}/libnss_libvirt*.so.*
%{_datadir}/augeas/lenses/*virt*
%exclude %{_datadir}/augeas/lenses/libvirtd_qemu.aug
%exclude %{_datadir}/augeas/lenses/virtqemud.aug
%exclude %{_datadir}/augeas/lenses/libvirtd_lxc.aug
%exclude %{_datadir}/augeas/lenses/virtlxcd.aug
%exclude %{_datadir}/augeas/lenses/virtstoraged.aug
%{_datadir}/augeas/lenses/tests/*virt*
%exclude %{_datadir}/augeas/lenses/tests/test_libvirtd_qemu.aug
%exclude %{_datadir}/augeas/lenses/tests/test_virtqemud.aug
%exclude %{_datadir}/augeas/lenses/tests/test_libvirtd_lxc.aug
%exclude %{_datadir}/augeas/lenses/tests/test_virtlxcd.aug
%exclude %{_datadir}/augeas/lenses/tests/test_virtstoraged.aug
%{_sysconfdir}/libvirt/
%exclude %{_sysconfdir}/libvirt/libvirt.conf
%exclude %{_sysconfdir}/libvirt/virt-login-shell.conf
%exclude %{_sysconfdir}/libvirt/virtqemud.conf
%exclude %{_sysconfdir}/libvirt/qemu.conf
%exclude %{_sysconfdir}/libvirt/qemu-lockd.conf
%exclude %{_sysconfdir}/libvirt/qemu/
%exclude %{_sysconfdir}/libvirt/virtlxcd.conf
%exclude %{_sysconfdir}/libvirt/lxc.conf
%exclude %{_sysconfdir}/libvirt/lxc/
%exclude %{_sysconfdir}/libvirt/virtstoraged.conf
%exclude %{_sysconfdir}/libvirt/storage/
%{_sysconfdir}/logrotate.d/*virt*
%exclude %{_sysconfdir}/logrotate.d/libvirtd.qemu
%exclude %{_sysconfdir}/logrotate.d/libvirtd.lxc
%{_prefix}/lib/firewalld/policies/*libvirt*.xml
%{_prefix}/lib/firewalld/zones/*libvirt*.xml
%{_datadir}/systemtap/tapset/*libvirt*.stp
%{_unitdir}/*virt*.service
%exclude %{_unitdir}/virtqemud.service
%exclude %{_unitdir}/virtlxcd.service
%exclude %{_unitdir}/virtstoraged.service
%{_unitdir}/*virt*.socket
%exclude %{_unitdir}/virtqemud.socket
%exclude %{_unitdir}/virtqemud-ro.socket
%exclude %{_unitdir}/virtqemud-admin.socket
%exclude %{_unitdir}/virtlxcd.socket
%exclude %{_unitdir}/virtlxcd-ro.socket
%exclude %{_unitdir}/virtlxcd-admin.socket
%exclude %{_unitdir}/virtstoraged.socket
%exclude %{_unitdir}/virtstoraged-ro.socket
%exclude %{_unitdir}/virtstoraged-admin.socket
%{_mandir}/man8/*virt*.8*
%exclude %{_mandir}/man8/libvirtd.8*
%exclude %{_mandir}/man8/virtqemud.8*
%exclude %{_mandir}/man8/virtlxcd.8*
%exclude %{_mandir}/man8/virtstoraged.8*

%files devel
%{_includedir}/libvirt/
%{_libdir}/libvirt*.so
%{_libdir}/pkgconfig/libvirt-admin.pc
%{_libdir}/pkgconfig/libvirt-lxc.pc
%{_libdir}/pkgconfig/libvirt-qemu.pc
%{_libdir}/pkgconfig/libvirt.pc
%{_datadir}/libvirt/api/

%changelog
%autochangelog
