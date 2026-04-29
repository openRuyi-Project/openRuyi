# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond rdma 1
%bcond make_check 0
%bcond ceph_test_package 1
%bcond rbd_ssd_cache 1
%bcond cephadm_pip_deps 1
%bcond system_utf8proc 1
%bcond system_arrow 0
%bcond lttng 1
%bcond libradosstriper 1
%bcond cephfs_shell 1
%bcond amqp_endpoint 1
%bcond kafka_endpoint 1
%bcond tcmalloc 1
%bcond lua_packages 1
%bcond jaeger 1
%bcond manpages 1
%bcond ocf 1

%define _lto_cflags %{nil}

Name:           ceph
Version:        20.2.0
Release:        %autorelease
Summary:        User space components of the Ceph file system
License:        LGPL-2.1-or-later AND LGPL-3.0-only AND CC-BY-SA-3.0 AND GPL-2.0-only AND BSL-1.0 AND BSD-2-Clause AND BSD-3-Clause AND MIT
URL:            http://ceph.com/
VCS:            git:https://github.com/ceph/ceph
#!RemoteAsset:  sha256:8de064d69831ef327339539f233c78ec827fa351c40ced9a9916f0b4174c6685
Source:         https://download.ceph.com/tarballs/ceph-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DWITH_SYSTEM_ZSTD:BOOL=ON
%if %{with jaeger}
BuildOption(conf):  -DWITH_JAEGER:BOOL=ON
%else
BuildOption(conf):  -DWITH_JAEGER:BOOL=OFF
%endif
BuildOption(conf):  -DWITH_RADOSGW_SELECT_PARQUET=OFF
BuildOption(conf):  -DWITH_RADOSGW_ARROW_FLIGHT=OFF
%if %{with rdma}
BuildOption(conf):  -DWITH_RDMA=ON
%else
BuildOption(conf):  -DWITH_RDMA=OFF
%endif
BuildOption(conf):  -GNinja
BuildOption(conf):  -DBUILD_CONFIG=rpmbuild
BuildOption(conf):  -DSYSTEMD_SYSTEM_UNIT_DIR:PATH=%{_unitdir}
BuildOption(conf):  -DCMAKE_INSTALL_SYSCONFDIR:PATH=%{_sysconfdir}
%if %{with manpages}
BuildOption(conf):  -DWITH_MANPAGE:BOOL=ON
%else
BuildOption(conf):  -DWITH_MANPAGE:BOOL=OFF
%endif
BuildOption(conf):  -DWITH_PYTHON3:STRING=3
BuildOption(conf):  -DWITH_MGR_DASHBOARD_FRONTEND:BOOL=OFF
%if %{without ceph_test_package}
BuildOption(conf):  -DWITH_TESTS:BOOL=OFF
%endif
%if %{with lttng}
BuildOption(conf):  -DWITH_LTTNG:BOOL=ON
BuildOption(conf):  -DWITH_BABELTRACE:BOOL=ON
%else
BuildOption(conf):  -DWITH_LTTNG:BOOL=OFF
BuildOption(conf):  -DWITH_BABELTRACE:BOOL=OFF
%endif
%if %{with ocf}
BuildOption(conf):  -DWITH_OCF:BOOL=ON
%endif
BuildOption(conf):  -DWITH_SYSTEM_LIBURING:BOOL=ON
BuildOption(conf):  -DWITH_SYSTEM_BOOST:BOOL=OFF
%if %{with libradosstriper}
BuildOption(conf):  -DWITH_LIBRADOSSTRIPER:BOOL=ON
%else
BuildOption(conf):  -DWITH_LIBRADOSSTRIPER:BOOL=OFF
%endif
%if %{with cephfs_shell}
BuildOption(conf):  -DWITH_CEPHFS_SHELL:BOOL=ON
%endif
%if %{with amqp_endpoint}
BuildOption(conf):  -DWITH_RADOSGW_AMQP_ENDPOINT:BOOL=ON
%else
BuildOption(conf):  -DWITH_RADOSGW_AMQP_ENDPOINT:BOOL=OFF
%endif
%if %{with kafka_endpoint}
BuildOption(conf):  -DWITH_RADOSGW_KAFKA_ENDPOINT:BOOL=ON
%else
BuildOption(conf):  -DWITH_RADOSGW_KAFKA_ENDPOINT:BOOL=OFF
%endif
%if %{with tcmalloc}
BuildOption(conf):  -DALLOCATOR:STRING=tcmalloc
%else
BuildOption(conf):  -DALLOCATOR:STRING=libc
%endif
%if %{without lua_packages}
BuildOption(conf):  -DWITH_RADOSGW_LUA_PACKAGES:BOOL=OFF
%endif
%if %{with rbd_ssd_cache}
BuildOption(conf):  -DWITH_RBD_SSD_CACHE:BOOL=ON
%endif
BuildOption(conf):  -DBOOST_J:STRING=%{_smp_build_ncpus}
BuildOption(conf):  -Dxsimd_SOURCE="SYSTEM"
BuildOption(conf):  -DWITH_SYSTEM_UTF8PROC:BOOL=ON
BuildOption(conf):  -DWITH_QATDRV:BOOL=OFF
BuildOption(conf):  -DWITH_QATLIB:BOOL=OFF
BuildOption(conf):  -DWITH_QATZIP:BOOL=OFF
BuildOption(conf):  -DWITH_GRAFANA:BOOL=ON
BuildOption(conf):  -DCEPHADM_BUNDLED_DEPENDENCIES=none

BuildRequires:  pkgconfig(libzstd)
BuildRequires:  gperf
BuildRequires:  cmake
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(grpc)
BuildRequires:  pkgconfig(libaio)
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(libcryptsetup)
BuildRequires:  pkgconfig(libnbd)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libcap-ng)
BuildRequires:  pkgconfig(liburing)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  oath-toolkit
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  patch
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  procps
BuildRequires:  python3
BuildRequires:  pkgconfig(python)
BuildRequires:  python-setuptools
BuildRequires:  python-Cython
BuildRequires:  snappy-devel
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  sudo
BuildRequires:  pkgconfig(udev)
BuildRequires:  which
BuildRequires:  xfsprogs-devel
BuildRequires:  nasm
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(lmdb)
%if %{with amqp_endpoint}
BuildRequires:  pkgconfig(librabbitmq)
%endif
%if %{with kafka_endpoint}
BuildRequires:  pkgconfig(rdkafka)
%endif
%if %{with tcmalloc}
BuildRequires:  pkgconfig(libtcmalloc) >= 2.6.2
%endif
%if %{with jaeger}
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(thrift)
%endif
%if %{with manpages}
BuildRequires:  python3dist(sphinx)
%endif
BuildRequires:  pkgconfig(re2)
BuildRequires:  pkgconfig(libutf8proc)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(libkeyutils)
%if %{with rdma}
BuildRequires:  pkgconfig(libibverbs)
BuildRequires:  pkgconfig(librdmacm)
%endif
%if %{with lttng}
BuildRequires:  pkgconfig(lttng-ust)
BuildRequires:  pkgconfig(babeltrace)
%endif
BuildRequires:  ninja
BuildRequires:  pkgconfig(ldap)
BuildRequires:  pkgconfig(numa)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  python-prettytable
BuildRequires:  python-pyyaml
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(expat)
BuildRequires:  python-rpm-macros

Requires:       ceph-osd%{?_isa} = %{version}-%{release}
Requires:       ceph-mds%{?_isa} = %{version}-%{release}
Requires:       ceph-mgr%{?_isa} = %{version}-%{release}
Requires:       ceph-mon%{?_isa} = %{version}-%{release}
Requires:       systemd
Requires(post): binutils
%if %{with lua_packages}
Requires:       luarocks
%endif

%patchlist
# Fix CRC32C Intel fast assembly: update copyright and add prefetch optimization
0001-src-common-crc32c_intel_fast.patch
# Add missing <ostream> include in bit_str.h for std::ostream support
0002-src-common-bitstr.h.patch
# Add CET (Control-flow Enforcement Technology) marker to crc32c_intel_fast_zero_asm.s for IBT/SHSTK compatibility
0003-CET-Add-CET-marker-to-crc32c_intel_fast_zero_asm.s.patch
# Add CET marker to isa-l x86-64 CRC32 assembly codes for IBT/SHSTK compatibility
0004-isa-l-CET-Add-CET-marker-to-x86-64-crc32-assembly-co.patch
# Add CET marker to spdk/isa-l x86-64 CRC32 assembly codes for IBT/SHSTK compatibility
0005-spdk-isa-l-CET-Add-CET-marker-to-x86-64-crc32-assemb.patch
# Fix tracing on x86_64: define STAP_SDT_ARG_CONSTRAINT to workaround SystemTap constraint issue
0006-src-tracing.patch
# Fix dbstore CMakeLists: make dbstore_lib a STATIC library and add global link dependency
0007-src-rgw-store-dbstore-CMakeLists.txt.patch
# GCC 13 compatibility: fix std::uint8_t/uint32_t qualified name issues in templates
0008-gcc-13.patch
# Add -fcf-protection compiler flag for x86_64 in Boost build configuration
0009-cmake-modules-BuildBoost.cmake.patch
# Add CET .note.gnu.property section to Boost context x86_64 assembly for IBT/SHSTK compatibility
0010-boost-asm.patch
# Cython 3 compatibility: add noexcept specifier to callback functions in rbd.pyx
0011-src-pybind-rbd-rbd.pyx.patch
# Python 3.13 compatibility: add extern declaration for removed PySys_SetPath API
0012-src-mgr-PyModule.cc.patch
# Fix PPC CRC32C assembly: use __ASSEMBLY__ define instead of CRC32_CONSTANTS_HEADER
0013_src_common_crc32c_ppc_asm.S.patch
# OpenSSL 3.x compatibility: conditionally include deprecated engine.h header
0014-openssl-no-engine.patch
# Add missing <cstdint> include in RocksDB headers for uint64_t type
0015-src-rocksdb-db-blob-blob_file_meta.h.patch
# Disable shared library build and version properties in googletest to fix linking issues
0016-src-googletest-nosharedlibs.patch
# Fix tracing CMakeLists: set C99 extension compile option to gnu23 for compatibility
0017-src-tracing.patch
# Add missing GTEST_DISALLOW_COPY/MOVE_AND_ASSIGN_ macros for newer googletest compatibility
0018-src-test-neorados-common_tests.h.patch
# Apache Arrow 20.0.0 compatibility: add encryption_internal_19.h and update s3select API
0019-libarrow-20.0.0.patch
# Fix libcephfs linking: add missing common library dependency
0020-src-CMakeLists.txt.patch
# C++20/23 compatibility: replace deprecated <ciso646> with <iso646.h> in opentelemetry
0021-iso646.patch
# Bump bundled opentelemetry-cpp cmake_minimum_required from 3.1 to 3.5 (CMake 4.x dropped <3.5 compat)
0022-src-jaegertracing-opentelemetry-cpp-CMakeLists.txt.patch

%description
Ceph is a massively scalable, open-source, distributed storage system that runs
on commodity hardware and delivers object, block and file system storage.

%package        base
Summary:        Ceph Base Package
Provides:       ceph-test:/usr/bin/ceph-kvstore-tool
Requires:       ceph-common%{?_isa} = %{version}-%{release}
Requires:       findutils
Requires:       grep
Requires:       logrotate
Requires:       psmisc
Requires:       util-linux
Requires:       which

%description    base
Base is the package that includes all the files shared amongst ceph servers

%package     -n cephadm
Summary:        Utility to bootstrap Ceph clusters
Requires:       lvm2
Requires:       python3
Requires:       openssh-server
Requires:       which
Requires:       python3dist(jinja2) >= 2.10
Requires:       python3dist(pyyaml)

%description -n cephadm
Utility to bootstrap a Ceph cluster and manage Ceph daemons deployed
with systemd and podman.

%if %{with cephfs_shell}
%package     -n cephfs-shell
Summary:        Interactive shell for Ceph file system
Requires:       python3dist(cmd2)
Requires:       python3dist(colorama)
Requires:       python-cephfs%{?_isa} = %{version}-%{release}

%description -n cephfs-shell
This package contains an interactive tool that allows accessing a Ceph
file system without mounting it by providing a nice pseudo-shell which
works like an FTP client.
%endif

%package        common
Summary:        Ceph Common
Requires:       python-rados%{?_isa} = %{version}-%{release}
Requires:       python-rbd%{?_isa} = %{version}-%{release}
Requires:       python-cephfs%{?_isa} = %{version}-%{release}
Requires:       python-rgw%{?_isa} = %{version}-%{release}
Requires:       python-ceph-common = %{version}-%{release}
Requires:       python3dist(prettytable)
%{?systemd_requires}
Provides:       group(ceph)
Provides:       user(ceph)

%description    common
Common utilities to mount and interact with a ceph storage cluster.
Comprised of files that are common to Ceph clients and servers.

%package        mds
Summary:        Ceph Metadata Server Daemon
Requires:       ceph-base%{?_isa} = %{version}-%{release}

%description    mds
ceph-mds is the metadata server daemon for the Ceph distributed file system.
One or more instances of ceph-mds collectively manage the file system
namespace, coordinating access to the shared OSD cluster.

%package        mon
Summary:        Ceph Monitor Daemon
Provides:       ceph-test:/usr/bin/ceph-monstore-tool
Requires:       ceph-base%{?_isa} = %{version}-%{release}

%description    mon
ceph-mon is the cluster monitor daemon for the Ceph distributed file
system. One or more instances of ceph-mon form a Paxos part-time
parliament cluster that provides extremely reliable and durable storage
of cluster membership, configuration, and state.

%package        mgr
Summary:        Ceph Manager Daemon
Requires:       ceph-base%{?_isa} = %{version}-%{release}
Requires:       python3dist(bcrypt)
Requires:       python3dist(packaging)
Requires:       python3dist(pyopenssl)
Requires:       python3dist(requests)
Requires:       python3dist(python-dateutil)
Requires:       python3dist(setuptools)
Provides:       ceph-mgr-modules-core = %{version}-%{release}
Obsoletes:      ceph-mgr-modules-core < %{version}-%{release}

%description    mgr
ceph-mgr enables python modules that provide services (such as the REST
module derived from Calamari) and expose CLI hooks.  ceph-mgr gathers
the cluster maps, the daemon metadata, and performance counters, and
exposes all these to the python modules.

%package        mgr-dashboard
Summary:        Ceph Dashboard
Requires:       ceph-mgr%{?_isa} = %{version}-%{release}
Requires:       ceph-monitoring = %{version}-%{release}
Requires:       python3dist(numpy)
Requires:       python3dist(scipy)
Provides:       ceph-mgr-diskprediction-local = %{version}-%{release}
Obsoletes:      ceph-mgr-diskprediction-local < %{version}-%{release}

%description    mgr-dashboard
ceph-mgr-dashboard is a manager module, providing a web-based application
to monitor and manage many aspects of a Ceph cluster and related components.
See the Dashboard documentation at http://docs.ceph.com/ for details and a
detailed feature overview. This package also includes disk failure prediction
module using local algorithms and machine-learning databases.

%package        mgr-orchestration
Summary:        Ceph Manager orchestration modules
Requires:       ceph-mgr%{?_isa} = %{version}-%{release}
Requires:       cephadm = %{version}-%{release}
Requires:       python3dist(asyncssh)
Requires:       python3dist(natsort)
Requires:       python3dist(kubernetes)
Requires:       python3dist(jsonpatch)
Requires:       openssh-clients
Requires:       python3dist(jinja2)
Requires:       python3dist(cherrypy)
Provides:       ceph-mgr-cephadm = %{version}-%{release}
Obsoletes:      ceph-mgr-cephadm < %{version}-%{release}
Provides:       ceph-mgr-rook = %{version}-%{release}
Obsoletes:      ceph-mgr-rook < %{version}-%{release}
Provides:       ceph-mgr-k8sevents = %{version}-%{release}
Obsoletes:      ceph-mgr-k8sevents < %{version}-%{release}

%description    mgr-orchestration
ceph-mgr-orchestration provides orchestration modules for Ceph Manager,
including cephadm-based deployment, Rook-based Kubernetes orchestration,
and Kubernetes events integration.

%package        fuse
Summary:        Ceph fuse-based client
Requires:       fuse
Requires:       python3

%description    fuse
FUSE based client for Ceph distributed network file system

%package     -n rbd-mirror
Summary:        Ceph daemon for mirroring RBD images
Requires:       ceph-base%{?_isa} = %{version}-%{release}

%description -n rbd-mirror
Daemon for mirroring RBD images between Ceph clusters, streaming
changes asynchronously.

%package        radosgw
Summary:        Rados REST gateway
Requires:       ceph-base%{?_isa} = %{version}-%{release}
Requires:       mailcap

%description    radosgw
RADOS is a distributed object store used by the Ceph distributed
storage system.  This package provides a REST gateway to the
object store that aims to implement a superset of Amazon's S3
service as well as the OpenStack Object Storage ("Swift") API.

%if %{with ocf}
%package        resource-agents
Summary:        OCF-compliant resource agents for Ceph daemons
Requires:       ceph-base%{?_isa} = %{version}-%{release}
Requires:       resource-agents

%description    resource-agents
Resource agents for monitoring and managing Ceph daemons
under Open Cluster Framework (OCF) compliant resource
managers such as Pacemaker.
%endif

%package        osd
Summary:        Ceph Object Storage Daemon
Requires:       ceph-base%{?_isa} = %{version}-%{release}
Requires:       sudo
Requires:       libstoragemgmt
# volume deps (merged from ceph-volume)
Requires:       cryptsetup
Requires:       e2fsprogs
Requires:       lvm2
Requires:       parted
Requires:       util-linux
Requires:       xfsprogs
Requires:       python3dist(setuptools)
Requires:       python-ceph-common = %{version}-%{release}

%description    osd
ceph-osd is the object storage daemon for the Ceph distributed file
system.  It is responsible for storing objects on a local file system
and providing access to them over the network.

%package        devel
Summary:        Ceph development headers and libraries
Requires:       ceph-common%{?_isa} = %{version}-%{release}

%description    devel
This package contains headers and libraries needed to develop programs
that use Ceph distributed storage system, including RADOS object store,
RBD block device, RGW gateway, and CephFS distributed file system.

%package     -n python-rgw
Summary:        Python libraries for the RADOS gateway
Requires:       ceph-radosgw%{?_isa} = %{version}-%{release}
Requires:       python-rados%{?_isa} = %{version}-%{release}
Provides:       python3-rgw = %{version}-%{release}
%python_provide python3-rgw
Obsoletes:      python-rgw < %{version}-%{release}

%description -n python-rgw
This package contains Python libraries for interacting with Ceph RADOS
gateway.

%package     -n python-rados
Summary:        Python libraries for the RADOS object store
Requires:       python3
Requires:       ceph-common%{?_isa} = %{version}-%{release}
Provides:       python3-rados = %{version}-%{release}
%python_provide python3-rados
Obsoletes:      python-rados < %{version}-%{release}

%description -n python-rados
This package contains Python libraries for interacting with Ceph RADOS
object store.

%package     -n python-rbd
Summary:        Python libraries for the RADOS block device
Requires:       ceph-common%{?_isa} = %{version}-%{release}
Requires:       python-rados%{?_isa} = %{version}-%{release}
Provides:       python3-rbd = %{version}-%{release}
%python_provide python3-rbd
Obsoletes:      python-rbd < %{version}-%{release}

%description -n python-rbd
This package contains Python libraries for interacting with Ceph RADOS
block device.

%package     -n python-cephfs
Summary:        Python libraries for Ceph distributed file system
Requires:       ceph-common%{?_isa} = %{version}-%{release}
Requires:       python-rados%{?_isa} = %{version}-%{release}
Requires:       python-ceph-common = %{version}-%{release}
Provides:       python3-cephfs = %{version}-%{release}
%python_provide python3-cephfs
Obsoletes:      python-cephfs < %{version}-%{release}

%description -n python-cephfs
This package contains Python libraries for interacting with Ceph distributed
file system.

%package     -n python-ceph-common
Summary:        Python utility libraries for Ceph
Provides:       python3-ceph-common = %{version}-%{release}
%python_provide python3-ceph-common

%description -n python-ceph-common
This package contains data structures, classes and functions used by Ceph.
It also contains utilities used for the cephadm orchestrator, as well as
types and routines for the Ceph CLI and RESTful interface.

%if %{with ceph_test_package}
%package     -n ceph-test
Summary:        Ceph benchmarks and test tools
Requires:       ceph-common%{?_isa} = %{version}-%{release}
Requires:       xmlstarlet
Requires:       jq
Requires:       socat
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(gmock)

%description -n ceph-test
This package contains Ceph benchmarks and test tools.
%endif

%package        monitoring
Summary:        Ceph monitoring dashboards, alerts and SNMP MIB

%description    monitoring
This package provides Grafana dashboards, Prometheus alerts, and
SNMP MIB for monitoring Ceph clusters.

%prep -a
# Create two sysusers.d config files
cat >ceph.sysusers.conf <<EOF
g ceph 167
u ceph 167 'Ceph storage service' %{_localstatedir}/lib/ceph -
EOF
cat >cephadm.sysusers.conf <<EOF
u cephadm - 'cephadm user for mgr/cephadm' %{_sharedstatedir}/cephadm /bin/bash
EOF

%check
# no test

%install -a
# we have dropped sysvinit bits
rm -f %{buildroot}/%{_sysconfdir}/init.d/ceph

install -m 0644 -D src/etc-rbdmap %{buildroot}%{_sysconfdir}/ceph/rbdmap
install -m 0644 -D systemd/ceph.tmpfiles.d %{buildroot}%{_tmpfilesdir}/ceph-common.conf
install -m 0644 -D systemd/50-ceph.preset %{buildroot}%{_presetdir}/50-ceph.preset
mkdir -p %{buildroot}%{_sbindir}
install -m 0644 -D src/logrotate.conf %{buildroot}%{_sysconfdir}/logrotate.d/ceph
chmod 0644 %{buildroot}%{_docdir}/ceph/sample.ceph.conf
install -m 0644 -D COPYING %{buildroot}%{_docdir}/ceph/COPYING
install -m 0644 -D etc/sysctl/90-ceph-osd.conf %{buildroot}%{_sysctldir}/90-ceph-osd.conf
install -m 0755 -D src/tools/rbd_nbd/rbd-nbd_quiesce %{buildroot}%{_libexecdir}/rbd-nbd/rbd-nbd_quiesce

install -m 0644 -D ceph.sysusers.conf %{buildroot}%{_sysusersdir}/ceph.conf
install -m 0644 -D cephadm.sysusers.conf %{buildroot}%{_sysusersdir}/cephadm.conf

mkdir -p %{buildroot}%{_sharedstatedir}/cephadm
chmod 0700 %{buildroot}%{_sharedstatedir}/cephadm
mkdir -p %{buildroot}%{_sharedstatedir}/cephadm/.ssh
chmod 0700 %{buildroot}%{_sharedstatedir}/cephadm/.ssh
touch %{buildroot}%{_sharedstatedir}/cephadm/.ssh/authorized_keys
chmod 0600 %{buildroot}%{_sharedstatedir}/cephadm/.ssh/authorized_keys

# udev rules
install -m 0644 -D udev/50-rbd.rules %{buildroot}%{_udevrulesdir}/50-rbd.rules

# sudoers.d
install -m 0440 -D sudoers.d/ceph-smartctl %{buildroot}%{_sysconfdir}/sudoers.d/ceph-smartctl

%py3_shebang_fix %{buildroot}%{_bindir}/* %{buildroot}%{_sbindir}/*

#set up placeholder directories
mkdir -p %{buildroot}%{_sysconfdir}/ceph
mkdir -p %{buildroot}%{_localstatedir}/run/ceph
mkdir -p %{buildroot}%{_localstatedir}/log/ceph
mkdir -p %{buildroot}%{_localstatedir}/lib/ceph/tmp
mkdir -p %{buildroot}%{_localstatedir}/lib/ceph/mon
mkdir -p %{buildroot}%{_localstatedir}/lib/ceph/osd
mkdir -p %{buildroot}%{_localstatedir}/lib/ceph/mds
mkdir -p %{buildroot}%{_localstatedir}/lib/ceph/mgr
mkdir -p %{buildroot}%{_localstatedir}/lib/ceph/crash
mkdir -p %{buildroot}%{_localstatedir}/lib/ceph/crash/posted
mkdir -p %{buildroot}%{_localstatedir}/lib/ceph/radosgw
mkdir -p %{buildroot}%{_localstatedir}/lib/ceph/bootstrap-osd
mkdir -p %{buildroot}%{_localstatedir}/lib/ceph/bootstrap-mds
mkdir -p %{buildroot}%{_localstatedir}/lib/ceph/bootstrap-rgw
mkdir -p %{buildroot}%{_localstatedir}/lib/ceph/bootstrap-mgr
mkdir -p %{buildroot}%{_localstatedir}/lib/ceph/bootstrap-rbd
mkdir -p %{buildroot}%{_localstatedir}/lib/ceph/bootstrap-rbd-mirror

# prometheus alerts
install -m 644 -D monitoring/ceph-mixin/prometheus_alerts.yml %{buildroot}/etc/prometheus/ceph/ceph_default_alerts.yml

# grafana charts
install -m 644 -D monitoring/ceph-mixin/dashboards_out/* %{buildroot}/etc/grafana/dashboards/ceph-dashboard/

# SNMP MIB
install -m 644 -D -t %{buildroot}%{_datadir}/snmp/mibs monitoring/snmp/CEPH-MIB.txt

mv %{buildroot}%{_exec_prefix}/sbin/ceph-create-keys %{buildroot}%{_bindir}/

%files

%files base
%{_bindir}/ceph-crash
%{_bindir}/crushtool
%{_bindir}/monmaptool
%{_bindir}/osdmaptool
%{_bindir}/ceph-kvstore-tool
%{_bindir}/ceph-run
%{_presetdir}/50-ceph.preset
%{_bindir}/ceph-create-keys
%dir %{_libexecdir}/ceph
%{_libexecdir}/ceph/ceph_common.sh
%dir %{_libdir}/rados-classes
%{_libdir}/rados-classes/*
%dir %{_libdir}/ceph
%dir %{_libdir}/ceph/erasure-code
%{_libdir}/ceph/erasure-code/libec_*.so*
%dir %{_libdir}/ceph/extblkdev
%{_libdir}/ceph/extblkdev/libceph_*.so*
%dir %{_libdir}/ceph/compressor
%{_libdir}/ceph/compressor/libceph_*.so*
%{_unitdir}/ceph-crash.service
%dir %{_libdir}/ceph/crypto
%{_libdir}/ceph/crypto/libceph_*.so*
%if %{with lttng}
%{_libdir}/libos_tp.so*
%{_libdir}/libosd_tp.so*
%{_libdir}/libmgr_op_tp.so*
%endif
%config(noreplace) %{_sysconfdir}/logrotate.d/ceph
%{_unitdir}/ceph.target
#set up placeholder directories
%attr(750,ceph,ceph) %dir %{_localstatedir}/lib/ceph/crash
%attr(750,ceph,ceph) %dir %{_localstatedir}/lib/ceph/crash/posted
%attr(750,ceph,ceph) %dir %{_localstatedir}/lib/ceph/tmp
%attr(750,ceph,ceph) %dir %{_localstatedir}/lib/ceph/bootstrap-osd
%attr(750,ceph,ceph) %dir %{_localstatedir}/lib/ceph/bootstrap-mds
%attr(750,ceph,ceph) %dir %{_localstatedir}/lib/ceph/bootstrap-rgw
%attr(750,ceph,ceph) %dir %{_localstatedir}/lib/ceph/bootstrap-mgr
%attr(750,ceph,ceph) %dir %{_localstatedir}/lib/ceph/bootstrap-rbd
%attr(750,ceph,ceph) %dir %{_localstatedir}/lib/ceph/bootstrap-rbd-mirror
%{_sysconfdir}/sudoers.d/ceph-smartctl
# ceph-exporter (merged)
%{_bindir}/ceph-exporter
%{_unitdir}/ceph-exporter.service
# immutable-object-cache (merged)
%{_bindir}/ceph-immutable-object-cache
%{_unitdir}/ceph-immutable-object-cache@.service
%{_unitdir}/ceph-immutable-object-cache.target
# node-proxy (merged)
%{_sbindir}/ceph-node-proxy
%dir %{python3_sitelib}/ceph_node_proxy
%{python3_sitelib}/ceph_node_proxy/*
%{python3_sitelib}/ceph_node_proxy-*
%if %{with manpages}
%{_mandir}/man8/ceph-create-keys.8*
%{_mandir}/man8/ceph-run.8*
%{_mandir}/man8/crushtool.8*
%{_mandir}/man8/osdmaptool.8*
%{_mandir}/man8/monmaptool.8*
%{_mandir}/man8/ceph-kvstore-tool.8*
%{_mandir}/man8/ceph-immutable-object-cache.8*
%endif

%post base
%systemd_post ceph.target ceph-crash.service ceph-exporter.service ceph-immutable-object-cache@.service ceph-immutable-object-cache.target

%preun base
%systemd_preun ceph-exporter.service ceph-immutable-object-cache@.service ceph-immutable-object-cache.target

%postun base
%systemd_postun ceph.target ceph-immutable-object-cache@.service ceph-immutable-object-cache.target
if [ $1 -ge 1 ] ; then
  SYSCONF_CEPH=%{_sysconfdir}/sysconfig/ceph
  if [ -f $SYSCONF_CEPH -a -r $SYSCONF_CEPH ] ; then
    source $SYSCONF_CEPH
  fi
  if [ "X$CEPH_AUTO_RESTART_ON_UPGRADE" = "Xyes" ] ; then
    /usr/bin/systemctl try-restart ceph-immutable-object-cache@.service > /dev/null 2>&1 || :
  fi
fi

%files -n cephadm
%{_sbindir}/cephadm
%attr(0700,cephadm,cephadm) %dir %{_sharedstatedir}/cephadm
%attr(0700,cephadm,cephadm) %dir %{_sharedstatedir}/cephadm/.ssh
%config(noreplace) %attr(0600,cephadm,cephadm) %{_sharedstatedir}/cephadm/.ssh/authorized_keys
%{_sysusersdir}/cephadm.conf
%if %{with manpages}
%{_mandir}/man8/cephadm.8*
%endif

%preun common
%systemd_preun ceph.target ceph-crash.service

%files common
%dir %{_docdir}/ceph
%doc %{_docdir}/ceph/sample.ceph.conf
%license %{_docdir}/ceph/COPYING
%{_bindir}/ceph
%{_bindir}/ceph-authtool
%{_bindir}/ceph-conf
%{_bindir}/ceph-dencoder
%{_bindir}/ceph-rbdnamer
%{_bindir}/ceph-syn
%{_bindir}/cephfs-data-scan
%{_bindir}/cephfs-journal-tool
%{_bindir}/cephfs-table-tool
%{_bindir}/crushdiff
%{_bindir}/rados
%{_bindir}/radosgw-admin
%{_bindir}/rbd
%{_bindir}/rbd-replay
%{_bindir}/rbd-replay-many
%{_bindir}/rbdmap
%{_bindir}/rgw-gap-list
%{_bindir}/rgw-gap-list-comparator
%{_bindir}/rgw-orphan-list
%{_bindir}/rgw-restore-bucket-index
%{_sbindir}/mount.ceph

%if %{with lttng}
%{_bindir}/rbd-replay-prep
%endif
%{_bindir}/ceph-post-file
%dir %{_libdir}/ceph/denc
%{_libdir}/ceph/denc/denc-mod-*.so
%{_tmpfilesdir}/ceph-common.conf
%dir %{_datadir}/ceph/
%{_datadir}/ceph/known_hosts_drop.ceph.com
%{_datadir}/ceph/id_rsa_drop.ceph.com
%{_datadir}/ceph/id_rsa_drop.ceph.com.pub
%dir %{_sysconfdir}/ceph/
%config %{_sysconfdir}/bash_completion.d/ceph
%config %{_sysconfdir}/bash_completion.d/rados
%config %{_sysconfdir}/bash_completion.d/rbd
%config %{_sysconfdir}/bash_completion.d/radosgw-admin
%config(noreplace) %{_sysconfdir}/ceph/rbdmap
%{_unitdir}/rbdmap.service
%dir %{_udevrulesdir}
%{_udevrulesdir}/50-rbd.rules
%attr(3770,ceph,ceph) %dir %{_localstatedir}/log/ceph/
%attr(750,ceph,ceph) %dir %{_localstatedir}/lib/ceph/
%{_sysusersdir}/ceph.conf
# librados runtime libs (merged from librados2)
%{_libdir}/librados.so.*
%dir %{_libdir}/ceph
%{_libdir}/ceph/libceph-common.so.*
%if %{with lttng}
%{_libdir}/librados_tp.so.*
%endif
# librbd runtime libs (merged from librbd1)
%{_libdir}/librbd.so.*
%if %{with lttng}
%{_libdir}/librbd_tp.so.*
%endif
%dir %{_libdir}/ceph/librbd
%{_libdir}/ceph/librbd/libceph_*.so*
# libcephfs runtime libs (merged from libcephfs2)
%{_libdir}/libcephfs.so.*
# libcephfs-proxy runtime libs (merged from libcephfs-proxy2)
%{_libdir}/libcephfs_proxy.so.*
# libcephfsd daemon (merged from libcephfs-daemon)
%{_sbindir}/libcephfsd
# libradosstriper runtime libs (merged from libradosstriper1)
%if %{with libradosstriper}
%{_libdir}/libradosstriper.so.*
%endif
# rbd-fuse (merged)
%{_bindir}/rbd-fuse
# rbd-nbd (merged)
%{_bindir}/rbd-nbd
%dir %{_libexecdir}/rbd-nbd
%{_libexecdir}/rbd-nbd/rbd-nbd_quiesce
# cephfs-top (merged)
%{python3_sitelib}/cephfs_top-*.egg-info
%{_bindir}/cephfs-top
%if %{with manpages}
%{_mandir}/man8/ceph-authtool.8*
%{_mandir}/man8/ceph-conf.8*
%{_mandir}/man8/ceph-dencoder.8*
%{_mandir}/man8/ceph-rbdnamer.8*
%{_mandir}/man8/ceph-syn.8*
%{_mandir}/man8/ceph-post-file.8*
%{_mandir}/man8/ceph.8*
%{_mandir}/man8/crushdiff.8*
%{_mandir}/man8/mount.ceph.8*
%{_mandir}/man8/rados.8*
%{_mandir}/man8/radosgw-admin.8*
%{_mandir}/man8/rbd.8*
%{_mandir}/man8/rbdmap.8*
%{_mandir}/man8/rbd-replay.8*
%{_mandir}/man8/rbd-replay-many.8*
%{_mandir}/man8/rbd-replay-prep.8*
%{_mandir}/man8/rgw-orphan-list.8*
%{_mandir}/man8/rgw-gap-list.8*
%{_mandir}/man8/rgw-restore-bucket-index.8*
%{_mandir}/man8/rbd-fuse.8*
%{_mandir}/man8/rbd-nbd.8*
%{_mandir}/man8/cephfs-top.8*
%endif

%if %{with cephfs_shell}
%files -n cephfs-shell
%{python3_sitelib}/cephfs_shell-*.egg-info
%{_bindir}/cephfs-shell
%if %{with manpages}
%{_mandir}/man8/cephfs-shell.8*
%endif
%endif

%pre common
CEPH_GROUP_ID=167
CEPH_USER_ID=167
/usr/sbin/groupadd ceph -g $CEPH_GROUP_ID -o -r 2>/dev/null || :
/usr/sbin/useradd ceph -u $CEPH_USER_ID -o -r -g ceph -s /sbin/nologin -c "Ceph daemons" -d %{_localstatedir}/lib/ceph 2>/dev/null || :
exit 0

%post common
%tmpfiles_create %{_tmpfilesdir}/ceph-common.conf

%postun common
# Package removal cleanup
if [ "$1" -eq "0" ] ; then
    rm -rf %{_localstatedir}/log/ceph
    rm -rf %{_sysconfdir}/ceph
fi

%files mds
%{_bindir}/ceph-mds
%{_unitdir}/ceph-mds@.service
%{_unitdir}/ceph-mds.target
%attr(750,ceph,ceph) %dir %{_localstatedir}/lib/ceph/mds
# cephfs-mirror (merged)
%{_bindir}/cephfs-mirror
%{_unitdir}/cephfs-mirror@.service
%{_unitdir}/cephfs-mirror.target
%if %{with manpages}
%{_mandir}/man8/ceph-mds.8*
%{_mandir}/man8/cephfs-mirror.8*
%endif

%post mds
%systemd_post ceph-mds@.service ceph-mds.target cephfs-mirror@.service cephfs-mirror.target

%preun mds
%systemd_preun ceph-mds@.service ceph-mds.target cephfs-mirror@.service cephfs-mirror.target

%postun mds
%systemd_postun ceph-mds@.service ceph-mds.target cephfs-mirror@.service cephfs-mirror.target
if [ $1 -ge 1 ] ; then
  # Restart on upgrade, but only if "CEPH_AUTO_RESTART_ON_UPGRADE" is set to
  # "yes". In any case: if units are not running, do not touch them.
  SYSCONF_CEPH=%{_sysconfdir}/sysconfig/ceph
  if [ -f $SYSCONF_CEPH -a -r $SYSCONF_CEPH ] ; then
    source $SYSCONF_CEPH
  fi
  if [ "X$CEPH_AUTO_RESTART_ON_UPGRADE" = "Xyes" ] ; then
    /usr/bin/systemctl try-restart ceph-mds@.service cephfs-mirror@.service > /dev/null 2>&1 || :
  fi
fi

%files mgr
%{_bindir}/ceph-mgr
%dir %{_datadir}/ceph/mgr
%{_datadir}/ceph/mgr/mgr_module.*
%{_datadir}/ceph/mgr/mgr_util.*
%{_datadir}/ceph/mgr/object_format.*
%{_unitdir}/ceph-mgr@.service
%{_unitdir}/ceph-mgr.target
%attr(750,ceph,ceph) %dir %{_localstatedir}/lib/ceph/mgr
%{_libdir}/libcephsqlite.so
%{_datadir}/ceph/mgr/alerts
%{_datadir}/ceph/mgr/balancer
%{_datadir}/ceph/mgr/crash
%{_datadir}/ceph/mgr/devicehealth
%{_datadir}/ceph/mgr/influx
%{_datadir}/ceph/mgr/insights
%{_datadir}/ceph/mgr/iostat
%{_datadir}/ceph/mgr/localpool
%{_datadir}/ceph/mgr/mds_autoscaler
%{_datadir}/ceph/mgr/mirroring
%{_datadir}/ceph/mgr/nfs
%{_datadir}/ceph/mgr/orchestrator
%{_datadir}/ceph/mgr/osd_perf_query
%{_datadir}/ceph/mgr/osd_support
%{_datadir}/ceph/mgr/pg_autoscaler
%{_datadir}/ceph/mgr/progress
%{_datadir}/ceph/mgr/prometheus
%{_datadir}/ceph/mgr/rbd_support
%{_datadir}/ceph/mgr/rgw
%{_datadir}/ceph/mgr/selftest
%{_datadir}/ceph/mgr/smb
%{_datadir}/ceph/mgr/snap_schedule
%{_datadir}/ceph/mgr/stats
%{_datadir}/ceph/mgr/status
%{_datadir}/ceph/mgr/telegraf
%{_datadir}/ceph/mgr/telemetry
%{_datadir}/ceph/mgr/test_orchestrator
%{_datadir}/ceph/mgr/volumes

%post mgr
%systemd_post ceph-mgr@.service ceph-mgr.target

%preun mgr
%systemd_preun ceph-mgr@.service ceph-mgr.target

%postun mgr
%systemd_postun ceph-mgr@.service ceph-mgr.target
if [ $1 -ge 1 ] ; then
  # Restart on upgrade, but only if "CEPH_AUTO_RESTART_ON_UPGRADE" is set to
  # "yes". In any case: if units are not running, do not touch them.
  SYSCONF_CEPH=%{_sysconfdir}/sysconfig/ceph
  if [ -f $SYSCONF_CEPH -a -r $SYSCONF_CEPH ] ; then
    source $SYSCONF_CEPH
  fi
  if [ "X$CEPH_AUTO_RESTART_ON_UPGRADE" = "Xyes" ] ; then
    /usr/bin/systemctl try-restart ceph-mgr@.service > /dev/null 2>&1 || :
  fi
fi

%files mgr-dashboard
%{_datadir}/ceph/mgr/dashboard
# diskprediction_local (merged from ceph-mgr-diskprediction-local)
%{_datadir}/ceph/mgr/diskprediction_local

%files mgr-orchestration
# cephadm module (merged from ceph-mgr-cephadm)
%{_datadir}/ceph/mgr/cephadm
# rook module (merged from ceph-mgr-rook)
%{_datadir}/ceph/mgr/rook
# k8sevents module (merged from ceph-mgr-k8sevents)
%{_datadir}/ceph/mgr/k8sevents

%files mon
%{_bindir}/ceph-mon
%{_bindir}/ceph-monstore-tool
%{_unitdir}/ceph-mon@.service
%{_unitdir}/ceph-mon.target
%attr(750,ceph,ceph) %dir %{_localstatedir}/lib/ceph/mon
%if %{with manpages}
%{_mandir}/man8/ceph-mon.8*
%endif

%post mon
%systemd_post ceph-mon@.service ceph-mon.target

%preun mon
%systemd_preun ceph-mon@.service ceph-mon.target

%postun mon
%systemd_postun ceph-mon@.service ceph-mon.target
if [ $1 -ge 1 ] ; then
  # Restart on upgrade, but only if "CEPH_AUTO_RESTART_ON_UPGRADE" is set to
  # "yes". In any case: if units are not running, do not touch them.
  SYSCONF_CEPH=%{_sysconfdir}/sysconfig/ceph
  if [ -f $SYSCONF_CEPH -a -r $SYSCONF_CEPH ] ; then
    source $SYSCONF_CEPH
  fi
  if [ "X$CEPH_AUTO_RESTART_ON_UPGRADE" = "Xyes" ] ; then
    /usr/bin/systemctl try-restart ceph-mon@.service > /dev/null 2>&1 || :
  fi
fi

%files fuse
%{_bindir}/ceph-fuse
%{_sbindir}/mount.fuse.ceph
%{_unitdir}/ceph-fuse@.service
%{_unitdir}/ceph-fuse.target
%if %{with manpages}
%{_mandir}/man8/ceph-fuse.8*
%{_mandir}/man8/mount.fuse.ceph.8*
%endif

%files -n rbd-mirror
%{_bindir}/rbd-mirror
%{_unitdir}/ceph-rbd-mirror@.service
%{_unitdir}/ceph-rbd-mirror.target
%if %{with manpages}
%{_mandir}/man8/rbd-mirror.8*
%endif

%post -n rbd-mirror
%systemd_post ceph-rbd-mirror@.service ceph-rbd-mirror.target

%preun -n rbd-mirror
%systemd_preun ceph-rbd-mirror@.service ceph-rbd-mirror.target

%postun -n rbd-mirror
%systemd_postun ceph-rbd-mirror@.service ceph-rbd-mirror.target
if [ $1 -ge 1 ] ; then
  # Restart on upgrade, but only if "CEPH_AUTO_RESTART_ON_UPGRADE" is set to
  # "yes". In any case: if units are not running, do not touch them.
  SYSCONF_CEPH=%{_sysconfdir}/sysconfig/ceph
  if [ -f $SYSCONF_CEPH -a -r $SYSCONF_CEPH ] ; then
    source $SYSCONF_CEPH
  fi
  if [ "X$CEPH_AUTO_RESTART_ON_UPGRADE" = "Xyes" ] ; then
    /usr/bin/systemctl try-restart ceph-rbd-mirror@.service > /dev/null 2>&1 || :
  fi
fi

%files radosgw
%{_bindir}/ceph-diff-sorted
%{_bindir}/radosgw
%{_bindir}/radosgw-token
%{_bindir}/radosgw-es
%{_bindir}/radosgw-object-expirer
%{_bindir}/rgw-policy-check
%dir %{_localstatedir}/lib/ceph/radosgw
%{_unitdir}/ceph-radosgw@.service
%{_unitdir}/ceph-radosgw.target
# librgw runtime libs (merged from librgw2)
%{_libdir}/librgw.so.*
%if %{with lttng}
%{_libdir}/librgw_op_tp.so.*
%{_libdir}/librgw_rados_tp.so.*
%endif
%if %{with manpages}
%{_mandir}/man8/ceph-diff-sorted.8*
%{_mandir}/man8/radosgw.8*
%{_mandir}/man8/rgw-policy-check.8*
%endif

%post radosgw
%systemd_post ceph-radosgw@.service ceph-radosgw.target

%preun radosgw
%systemd_preun ceph-radosgw@.service ceph-radosgw.target

%postun radosgw
%systemd_postun ceph-radosgw@.service ceph-radosgw.target
if [ $1 -ge 1 ] ; then
  # Restart on upgrade, but only if "CEPH_AUTO_RESTART_ON_UPGRADE" is set to
  # "yes". In any case: if units are not running, do not touch them.
  SYSCONF_CEPH=%{_sysconfdir}/sysconfig/ceph
  if [ -f $SYSCONF_CEPH -a -r $SYSCONF_CEPH ] ; then
    source $SYSCONF_CEPH
  fi
  if [ "X$CEPH_AUTO_RESTART_ON_UPGRADE" = "Xyes" ] ; then
    /usr/bin/systemctl try-restart ceph-radosgw@.service > /dev/null 2>&1 || :
  fi
fi

%files osd
%{_bindir}/ceph-clsinfo
%{_bindir}/ceph-bluestore-tool
%{_bindir}/ceph-erasure-code-tool
%{_bindir}/ceph-objectstore-tool
%{_bindir}/ceph-osd
%{_libexecdir}/ceph/ceph-osd-prestart.sh
%{_unitdir}/ceph-osd@.service
%{_unitdir}/ceph-osd.target
%attr(750,ceph,ceph) %dir %{_localstatedir}/lib/ceph/osd
%config(noreplace) %{_sysctldir}/90-ceph-osd.conf
# volume (merged from ceph-volume)
%{_sbindir}/ceph-volume
%{_sbindir}/ceph-volume-systemd
%dir %{python3_sitelib}/ceph_volume
%{python3_sitelib}/ceph_volume/*
%{python3_sitelib}/ceph_volume-*
%{_unitdir}/ceph-volume@.service
%if %{with manpages}
%{_mandir}/man8/ceph-clsinfo.8*
%{_mandir}/man8/ceph-osd.8*
%{_mandir}/man8/ceph-bluestore-tool.8*
%{_mandir}/man8/ceph-volume.8*
%{_mandir}/man8/ceph-volume-systemd.8*
%endif

%post osd
%systemd_post ceph-osd@.service ceph-osd.target ceph-volume@.service
%sysctl_apply 90-ceph-osd.conf

%preun osd
%systemd_preun ceph-osd@.service ceph-osd.target ceph-volume@.service

%postun osd
%systemd_postun ceph-osd@.service ceph-volume@.service ceph-osd.target
if [ $1 -ge 1 ] ; then
  # Restart on upgrade, but only if "CEPH_AUTO_RESTART_ON_UPGRADE" is set to
  # "yes". In any case: if units are not running, do not touch them.
  SYSCONF_CEPH=%{_sysconfdir}/sysconfig/ceph
  if [ -f $SYSCONF_CEPH -a -r $SYSCONF_CEPH ] ; then
    source $SYSCONF_CEPH
  fi
  if [ "X$CEPH_AUTO_RESTART_ON_UPGRADE" = "Xyes" ] ; then
    /usr/bin/systemctl try-restart ceph-osd@.service ceph-volume@.service > /dev/null 2>&1 || :
  fi
fi

%if %{with ocf}

%files resource-agents
%dir %{_prefix}/lib/ocf
%dir %{_prefix}/lib/ocf/resource.d
%dir %{_prefix}/lib/ocf/resource.d/ceph
%attr(0755,-,-) %{_prefix}/lib/ocf/resource.d/ceph/rbd

%endif

%files devel
# librados C headers and unversioned symlink
%dir %{_includedir}/rados
%{_includedir}/rados/librados.h
%{_includedir}/rados/rados_types.h
%{_libdir}/librados.so
%if %{with lttng}
%{_libdir}/librados_tp.so
%endif
%{_bindir}/librados-config
# librados C++ headers
%{_includedir}/rados/buffer.h
%{_includedir}/rados/buffer_fwd.h
%{_includedir}/rados/crc32c.h
%{_includedir}/rados/inline_memory.h
%{_includedir}/rados/librados.hpp
%{_includedir}/rados/librados_fwd.hpp
%{_includedir}/rados/page.h
%{_includedir}/rados/rados_types.hpp
# librbd headers and unversioned symlink
%dir %{_includedir}/rbd
%{_includedir}/rbd/librbd.h
%{_includedir}/rbd/librbd.hpp
%{_includedir}/rbd/features.h
%{_libdir}/librbd.so
%if %{with lttng}
%{_libdir}/librbd_tp.so
%endif
# librgw headers and unversioned symlink
%{_includedir}/rados/librgw.h
%{_includedir}/rados/rgw_file.h
%{_libdir}/librgw.so
%if %{with lttng}
%{_libdir}/librgw_op_tp.so
%{_libdir}/librgw_rados_tp.so
%endif
# libcephfs headers and unversioned symlink
%dir %{_includedir}/cephfs
%{_includedir}/cephfs/libcephfs.h
%{_includedir}/cephfs/ceph_ll_client.h
%{_includedir}/cephfs/types.h
%dir %{_includedir}/cephfs/metrics
%{_includedir}/cephfs/metrics/Types.h
%{_libdir}/libcephfs.so
%{_libdir}/libcephfs_proxy.so
%{_libdir}/pkgconfig/cephfs.pc
# libcephsqlite headers
%{_includedir}/libcephsqlite.h
# rados objclass headers
%{_includedir}/rados/objclass.h
%if %{with libradosstriper}
# libradosstriper headers and unversioned symlink
%dir %{_includedir}/radosstriper
%{_includedir}/radosstriper/libradosstriper.h
%{_includedir}/radosstriper/libradosstriper.hpp
%{_libdir}/libradosstriper.so
%endif
%if %{with manpages}
%{_mandir}/man8/librados-config.8*
%endif

%files -n python-rados
%{python3_sitearch}/rados.cpython*.so
%{python3_sitearch}/rados-*.egg-info

%files -n python-rgw
%{python3_sitearch}/rgw.cpython*.so
%{python3_sitearch}/rgw-*.egg-info

%files -n python-rbd
%{python3_sitearch}/rbd.cpython*.so
%{python3_sitearch}/rbd-*.egg-info

%files -n python-cephfs
%{python3_sitearch}/cephfs.cpython*.so
%{python3_sitearch}/cephfs-*.egg-info

%files -n python-ceph-common
%{python3_sitelib}/ceph
%{python3_sitelib}/ceph-*.egg-info
# python-ceph-argparse (merged)
%{python3_sitelib}/ceph_argparse.py
%{python3_sitelib}/ceph_daemon.py

%if %{with ceph_test_package}
%files -n ceph-test
%{_bindir}/ceph-client-debug
%{_bindir}/ceph_bench_log
%{_bindir}/ceph_multi_stress_watch
%{_bindir}/ceph_erasure_code_benchmark
%{_bindir}/ceph_omapbench
%{_bindir}/ceph_objectstore_bench
%{_bindir}/ceph_perf_objectstore
%{_bindir}/ceph_perf_local
%{_bindir}/ceph_perf_msgr_client
%{_bindir}/ceph_perf_msgr_server
%{_bindir}/ceph_psim
%{_bindir}/ceph_radosacl
%{_bindir}/ceph_rgw_jsonparser
%{_bindir}/ceph_rgw_multiparser
%{_bindir}/ceph_scratchtool
%{_bindir}/ceph_scratchtoolpp
%{_bindir}/ceph_test_*
%{_bindir}/ceph-coverage
%{_bindir}/ceph-debugpack
%{_bindir}/ceph-dedup-tool
%{_bindir}/ceph-dedup-daemon
%dir %{_libdir}/ceph
%{_libdir}/ceph/ceph-monstore-update-crush.sh
%if %{with manpages}
%{_mandir}/man8/ceph-debugpack.8*
%endif
%endif

%files monitoring
# grafana dashboards
%attr(0755,root,root) %dir %{_sysconfdir}/grafana/dashboards/ceph-dashboard
%config %{_sysconfdir}/grafana/dashboards/ceph-dashboard/*
# prometheus alerts
%attr(0755,root,root) %dir %{_sysconfdir}/prometheus/ceph
%config %{_sysconfdir}/prometheus/ceph/ceph_default_alerts.yml
# SNMP MIB
%attr(0755,root,root) %dir %{_datadir}/snmp
%{_datadir}/snmp/mibs

%changelog
%autochangelog
