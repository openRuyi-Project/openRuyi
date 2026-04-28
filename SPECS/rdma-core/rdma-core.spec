# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global dracutlibdir %{_prefix}/lib/dracut/

%bcond systemd 1
%bcond pyverbs 1

Name:           rdma-core
Version:        60.0
Release:        %autorelease
Summary:        RDMA core userspace libraries and daemons
License:        BSD-2-Clause OR GPL-2.0-only
URL:            https://github.com/linux-rdma/rdma-core
#!RemoteAsset:  sha256:aa9ca1f5a9e356f770441f52254ddc70ff0a4df76a25383e422075eb730efb4b
Source:         https://github.com/linux-rdma/rdma-core/archive/v%{version}/rdma-core-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DCMAKE_MODULE_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,now"
BuildOption(conf):  -DCMAKE_INSTALL_LIBEXECDIR:PATH=%{_libexecdir}
BuildOption(conf):  -DCMAKE_INSTALL_LOCALSTATEDIR:PATH=%{_localstatedir}
BuildOption(conf):  -DCMAKE_INSTALL_SHAREDSTATEDIR:PATH=%{_sharedstatedir}
BuildOption(conf):  -DCMAKE_INSTALL_INFODIR:PATH=%{_infodir}
BuildOption(conf):  -DCMAKE_INSTALL_MODPROBEDIR:PATH=%{_modprobedir}
BuildOption(conf):  -DCMAKE_INSTALL_SYSCONFDIR:PATH=%{_sysconfdir}
BuildOption(conf):  -DCMAKE_INSTALL_SYSTEMD_SERVICEDIR:PATH=%{_unitdir}
BuildOption(conf):  -DCMAKE_INSTALL_SYSTEMD_BINDIR:PATH=%{_prefix}/lib/systemd
BuildOption(conf):  -DCMAKE_INSTALL_INITDDIR:PATH=%{_initddir}
BuildOption(conf):  -DCMAKE_INSTALL_RUNDIR:PATH=%{_rundir}
BuildOption(conf):  -DCMAKE_INSTALL_DOCDIR:PATH=%{_docdir}/%{name}-%{version}
BuildOption(conf):  -DCMAKE_INSTALL_UDEV_RULESDIR:PATH=%{_udevrulesdir}
BuildOption(conf):  -DCMAKE_INSTALL_PERLDIR:PATH=%{perl_vendorlib}
BuildOption(conf):  -DNO_MAN_PAGES=1
BuildOption(conf):  -DPYTHON_EXECUTABLE:PATH=%{__python3}
BuildOption(conf):  -DCMAKE_INSTALL_PYTHON_ARCH_LIB:PATH=%{python3_sitearch}
%if %{with pyverbs}
BuildOption(conf):  -DNO_PYVERBS=0
%else
BuildOption(conf):  -DNO_PYVERBS=1
%endif

BuildRequires:  binutils
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  ninja
# perl is needed for the proper rpm macros
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl-devel
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(udev)
%if %{with pyverbs}
BuildRequires:  libdrm-devel
BuildRequires:  python3-Cython
BuildRequires:  pkgconfig(python3)
%endif
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libnl-route-3.0)
BuildRequires:  pkgconfig(systemd)

Provides:       %{name}-libs = %{version}-%{release}
Provides:       libibverbs = %{version}-%{release}
Provides:       libibverbs%{?_isa} = %{version}-%{release}
Provides:       libibnetdisc = %{version}-%{release}
Provides:       libibmad = %{version}-%{release}
Provides:       libibumad = %{version}-%{release}
Provides:       librdmacm = %{version}-%{release}
Provides:       libefa = %{version}-%{release}
Provides:       libhns = %{version}-%{release}
Provides:       libmana = %{version}-%{release}
Provides:       libmlx4 = %{version}-%{release}
Provides:       libmlx5 = %{version}-%{release}

Requires:       kmod
Requires:       systemd
Requires:       udev

%description
RDMA core userspace infrastructure and documentation, including initialization
scripts, kernel driver-specific modprobe override configs, IPoIB network
scripts, dracut rules, and the rdma-ndd utility.

This package also includes all RDMA runtime libraries:
- libibverbs: Library for direct userspace use of RDMA hardware
- librdmacm: RDMA Connection Manager library
- libibumad: InfiniBand userspace management datagram library
- libibnetdisc: InfiniBand net discovery library
- libibmad: Low layer IB functions library
- Hardware-specific libraries: libefa, libhns, libmana, libmlx4, libmlx5

Device-specific plug-in ibverbs userspace drivers included:
- libcxgb4: Chelsio T4 iWARP HCA
- libefa: Amazon Elastic Fabric Adapter
- libhfi1: Intel Omni-Path HFI
- libhns: HiSilicon Hip08+ SoC
- libipathverbs: QLogic InfiniPath HCA
- libirdma: Intel Ethernet Connection RDMA
- libmana: Microsoft Azure Network Adapter
- libmlx4: Mellanox ConnectX-3 InfiniBand HCA
- libmlx5: Mellanox Connect-IB/X-4+ InfiniBand HCA
- libmthca: Mellanox InfiniBand HCA
- libocrdma: Emulex OneConnect RDMA/RoCE Device
- libqedr: QLogic QL4xxx RoCE HCA
- librxe: A software implementation of the RoCE protocol
- libsiw: A software implementation of the iWarp protocol
- libvmw_pvrdma: VMware paravirtual RDMA device

%package        devel
Summary:        RDMA core development libraries and headers
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
RDMA core development libraries and headers.

%package     -n libibverbs-utils
Summary:        Examples for the libibverbs library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n libibverbs-utils
Useful libibverbs example programs such as ibv_devinfo, which
displays information about RDMA devices.

%package     -n ibacm
Summary:        InfiniBand Communication Manager Assistant
%{?systemd_requires}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n ibacm
The ibacm daemon helps reduce the load of managing path record lookups on
large InfiniBand fabrics by providing a user space implementation of what
is functionally similar to an ARP cache.  The use of ibacm, when properly
configured, can reduce the SA packet load of a large IB cluster from O(n^2)
to O(n).  The ibacm daemon is started and normally runs in the background,
user applications need not know about this daemon as long as their app
uses librdmacm to handle connection bring up/tear down.  The librdmacm
library knows how to talk directly to the ibacm daemon to retrieve data.

%package     -n infiniband-diags
Summary:        InfiniBand Diagnostic Tools
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n infiniband-diags
diags provides IB diagnostic programs and scripts needed to diagnose an
IB subnet.

%package     -n iwpmd
Summary:        Userspace iWarp Port Mapper daemon
Requires:       %{name}%{?_isa} = %{version}-%{release}
%{?systemd_requires}

%description -n iwpmd
iwpmd provides a userspace service for iWarp drivers to claim
tcp ports through the standard socket interface.

%package     -n rsocket
Summary:        Preloadable library to turn the socket API RDMA-aware
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n rsocket
Existing applications can make use of rsockets through the use this
preloadable library. See the documentation in the packaged rsocket(7)
manpage for details.

%package     -n librdmacm-utils
Summary:        Examples for the librdmacm library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n librdmacm-utils
Example test programs for the librdmacm library.

%package     -n srp_daemon
Summary:        Tools for using the InfiniBand SRP protocol devices
Requires:       %{name}%{?_isa} = %{version}-%{release}
%{?systemd_requires}

%description -n srp_daemon
In conjunction with the kernel ib_srp driver, srp_daemon allows you to
discover and use SCSI devices via the SCSI RDMA Protocol over InfiniBand.

%package     -n rdma-ndd
Summary:        RDMA Node Description Daemon
Requires:       %{name}%{?_isa} = %{version}-%{release}
%{?systemd_requires}

%description -n rdma-ndd
rdma-ndd is a system daemon which watches for RDMA device changes and/or
hostname changes and updates the Node Description of the RDMA devices based
on those changes.

%if %{with pyverbs}
%package     -n python-pyverbs
Summary:        Python bindings for the libibverbs library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       python3-pyverbs
%python_provide python3-pyverbs

%description -n python-pyverbs
Python API over libibverbs that provides a user space interface for access
to RDMA devices.
%endif

%install -a
mkdir -p %{buildroot}/%{_sysconfdir}/rdma

mkdir -p %{buildroot}%{_udevrulesdir}
mkdir -p %{buildroot}%{dracutlibdir}/modules.d/50rdma
mkdir -p %{buildroot}%{_modprobedir}
mkdir -p %{buildroot}%{_unitdir}

# Port type setup for mlx4 dual port cards
install -D -m0644 redhat/rdma.mlx4.sys.modprobe %{buildroot}%{_modprobedir}/50-libmlx4.conf
install -D -m0644 redhat/rdma.mlx4.conf %{buildroot}/%{_sysconfdir}/rdma/mlx4.conf
chmod 0644 %{buildroot}%{_modprobedir}/mlx4.conf
install -D -m0755 redhat/rdma.mlx4-setup.sh %{buildroot}%{_libexecdir}/mlx4-setup.sh

# Dracut file for IB support during boot
install -D -m0644 kernel-boot/dracut/50rdma/module-setup.sh %{buildroot}%{dracutlibdir}/modules.d/50rdma/module-setup.sh

# ibacm
pushd %{__cmake_builddir}
LD_LIBRARY_PATH=./lib bin/ib_acme -D . -O
popd
install -D -m0644 %{__cmake_builddir}/ibacm_opts.cfg %{buildroot}%{_sysconfdir}/rdma/

# Delete the package's init.d scripts
rm -rf %{buildroot}/%{_initddir}/
rm -rf %{buildroot}/%{_sbindir}/srp_daemon.sh

%post
# we ship udev rules, so trigger an update.
%{_bindir}/udevadm trigger --subsystem-match=infiniband --action=change || true
%{_bindir}/udevadm trigger --subsystem-match=infiniband_mad --action=change || true

%post -n ibacm
%systemd_post ibacm.service ibacm.socket

%preun -n ibacm
%systemd_preun ibacm.service ibacm.socket

%postun -n ibacm
%systemd_postun ibacm.service ibacm.socket

%post -n srp_daemon
%systemd_post srp_daemon.service
# we ship udev rules, so trigger an update.
%{_bindir}/udevadm trigger --subsystem-match=infiniband_mad --action=change

%preun -n srp_daemon
%systemd_preun srp_daemon.service

%postun -n srp_daemon
%systemd_postun srp_daemon.service

%post -n iwpmd
%systemd_post iwpmd.service

%preun -n iwpmd
%systemd_preun iwpmd.service

%postun -n iwpmd
%systemd_postun iwpmd.service

%preun -n rdma-ndd
%systemd_preun rdma-ndd.service

%post -n rdma-ndd
%systemd_post rdma-ndd.service
# we ship udev rules, so trigger an update.
%{_bindir}/udevadm trigger --subsystem-match=infiniband --action=change || true

%postun -n rdma-ndd
%systemd_postun rdma-ndd.service

%files
%dir %{_sysconfdir}/rdma
%dir %{_sysconfdir}/rdma/modules
%dir %{_docdir}/rdma-core-%{version}
%dir %{_modprobedir}
%doc %{_docdir}/rdma-core-%{version}/70-persistent-ipoib.rules
%doc %{_docdir}/rdma-core-%{version}/README.md
%doc %{_docdir}/rdma-core-%{version}/udev.md
%doc %{_docdir}/rdma-core-%{version}/libibverbs.md
%doc %{_docdir}/rdma-core-%{version}/rxe.md
%doc %{_docdir}/rdma-core-%{version}/tag_matching.md
%doc %{_docdir}/rdma-core-%{version}/librdmacm.md
%config(noreplace) %{_sysconfdir}/rdma/mlx4.conf
%config(noreplace) %{_sysconfdir}/rdma/modules/infiniband.conf
%config(noreplace) %{_sysconfdir}/rdma/modules/iwarp.conf
%config(noreplace) %{_sysconfdir}/rdma/modules/opa.conf
%config(noreplace) %{_sysconfdir}/rdma/modules/rdma.conf
%config(noreplace) %{_sysconfdir}/rdma/modules/roce.conf
%{_modprobedir}/mlx4.conf
%{_modprobedir}/truescale.conf
%{_unitdir}/rdma-hw.target
%{_unitdir}/rdma-load-modules@.service
%dir %{dracutlibdir}
%dir %{dracutlibdir}/modules.d
%dir %{dracutlibdir}/modules.d/50rdma
%{dracutlibdir}/modules.d/50rdma/module-setup.sh
%{_udevrulesdir}/../rdma_rename
%{_udevrulesdir}/60-rdma-persistent-naming.rules
%{_udevrulesdir}/75-rdma-description.rules
%{_udevrulesdir}/90-rdma-hw-modules.rules
%{_udevrulesdir}/90-rdma-ulp-modules.rules
%{_udevrulesdir}/90-rdma-umad.rules
%{_modprobedir}/50-libmlx4.conf
%{_libexecdir}/mlx4-setup.sh
%{_libexecdir}/truescale-serdes.cmds
%license COPYING.*

# libibverbs runtime files
%dir %{_sysconfdir}/libibverbs.d
%dir %{_libdir}/libibverbs
%{_libdir}/libibverbs/*.so
%config(noreplace) %{_sysconfdir}/libibverbs.d/*.driver

# rdma core libs - libibverbs family
%{_libdir}/libibverbs*.so.*

# rdma core libs - connection management
%{_libdir}/librdmacm*.so.*

# rdma core libs - management datagram
%{_libdir}/libibumad*.so.*

# rdma core libs - diagnostic libs
%{_libdir}/libibnetdisc.so.*
%{_libdir}/libibmad.so.*

# hardware-specific libs - Amazon EFA
%{_libdir}/libefa*.so.*

# hardware-specific libs - HiSilicon HNS
%{_libdir}/libhns*.so.*

# hardware-specific libs - Microsoft Azure MANA
%{_libdir}/libmana*.so.*

# hardware-specific libs - Mellanox MLX4
%{_libdir}/libmlx4*.so.*

# hardware-specific libs - Mellanox MLX5
%{_libdir}/libmlx5*.so.*

%files devel
%doc %{_docdir}/rdma-core-%{version}/MAINTAINERS
%dir %{_includedir}/infiniband
%dir %{_includedir}/rdma
%{_includedir}/infiniband/*
%{_includedir}/rdma/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/libefa.pc
%{_libdir}/pkgconfig/libhns.pc
%{_libdir}/pkgconfig/libibmad.pc
%{_libdir}/pkgconfig/libibnetdisc.pc
%{_libdir}/pkgconfig/libibumad.pc
%{_libdir}/pkgconfig/libibverbs.pc
%{_libdir}/pkgconfig/libmana.pc
%{_libdir}/pkgconfig/libmlx4.pc
%{_libdir}/pkgconfig/libmlx5.pc
%{_libdir}/pkgconfig/librdmacm.pc

%files -n libibverbs-utils
%{_bindir}/ibv_*

%files -n ibacm
%config(noreplace) %{_sysconfdir}/rdma/ibacm_opts.cfg
%{_bindir}/ib_acme
%{_sbindir}/ibacm
%{_unitdir}/ibacm.service
%{_unitdir}/ibacm.socket
%dir %{_libdir}/ibacm
%{_libdir}/ibacm/*
%doc %{_docdir}/%{name}-%{version}/ibacm.md

%files -n infiniband-diags
%dir %{_sysconfdir}/infiniband-diags
%config(noreplace) %{_sysconfdir}/infiniband-diags/*
%{_sbindir}/ibaddr
%{_sbindir}/ibnetdiscover
%{_sbindir}/ibping
%{_sbindir}/ibportstate
%{_sbindir}/ibroute
%{_sbindir}/ibstat
%{_sbindir}/ibsysstat
%{_sbindir}/ibtracert
%{_sbindir}/perfquery
%{_sbindir}/sminfo
%{_sbindir}/smpdump
%{_sbindir}/smpquery
%{_sbindir}/saquery
%{_sbindir}/vendstat
%{_sbindir}/iblinkinfo
%{_sbindir}/ibqueryerrors
%{_sbindir}/ibcacheedit
%{_sbindir}/ibccquery
%{_sbindir}/ibccconfig
%{_sbindir}/dump_fts
%{_sbindir}/ibhosts
%{_sbindir}/ibswitches
%{_sbindir}/ibnodes
%{_sbindir}/ibrouters
%{_sbindir}/ibfindnodesusing.pl
%{_sbindir}/ibidsverify.pl
%{_sbindir}/check_lft_balance.pl
%{_sbindir}/dump_lfts.sh
%{_sbindir}/dump_mfts.sh
%{_sbindir}/ibstatus
%{perl_vendorlib}/IBswcountlimits.pm

%files -n iwpmd
%dir %{_sysconfdir}/rdma
%dir %{_sysconfdir}/rdma/modules
%{_sbindir}/iwpmd
%{_unitdir}/iwpmd.service
%config(noreplace) %{_sysconfdir}/rdma/modules/iwpmd.conf
%config(noreplace) %{_sysconfdir}/iwpmd.conf
%{_udevrulesdir}/90-iwpmd.rules

%files -n rsocket
%dir %{_libdir}/rsocket
%{_libdir}/rsocket/*.so*

%files -n librdmacm-utils
%{_bindir}/cmtime
%{_bindir}/mckey
%{_bindir}/rcopy
%{_bindir}/rdma_client
%{_bindir}/rdma_server
%{_bindir}/rdma_xclient
%{_bindir}/rdma_xserver
%{_bindir}/riostream
%{_bindir}/rping
%{_bindir}/rstream
%{_bindir}/ucmatose
%{_bindir}/udaddy
%{_bindir}/udpong

%files -n srp_daemon
%dir %{_libexecdir}/srp_daemon
%dir %{_sysconfdir}/rdma
%dir %{_sysconfdir}/rdma/modules
%config(noreplace) %{_sysconfdir}/srp_daemon.conf
%config(noreplace) %{_sysconfdir}/rdma/modules/srp_daemon.conf
%{_udevrulesdir}/60-srp_daemon.rules
%{_libexecdir}/srp_daemon/start_on_all_ports
%{_unitdir}/srp_daemon.service
%{_unitdir}/srp_daemon_port@.service
%{_sbindir}/ibsrpdm
%{_sbindir}/srp_daemon
%{_sbindir}/run_srp_daemon
%doc %{_docdir}/%{name}-%{version}/ibsrpdm.md

%files -n rdma-ndd
%{_sbindir}/rdma-ndd
%{_unitdir}/rdma-ndd.service
%{_udevrulesdir}/60-rdma-ndd.rules

%if %{with pyverbs}
%files -n python-pyverbs
%{python3_sitearch}/pyverbs
%dir %{_docdir}/rdma-core-%{version}/tests/
%{_docdir}/rdma-core-%{version}/tests/*.py
%endif

%changelog
%autochangelog
