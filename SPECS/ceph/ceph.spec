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
%bcond system_boost 0
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
%bcond spdk 0
%bcond crimson 0
%bcond seastar_dpdk 0

%define _lto_cflags %{nil}

%if %{with crimson}
# Seastar uses longjmp() to implement coroutine switching; that trips
# __longjmp_chk when _FORTIFY_SOURCE>=1. Upstream ceph.spec.in strips
# the -Wp,-D_FORTIFY_SOURCE=2 flag from CFLAGS/CXXFLAGS in %build for
# the same reason. Disabling the macro globally is the BuildSystem-
# friendly equivalent.
%global _fortify_level 0
%endif

# Submodule SHAs pinned by ceph.git@v21.0.0 (.gitmodules + tree).
%global sub_ceph_object_corpus          44b11dd5aa8a2f965ea395f13cf4cbb4a61e9afe
%global sub_ceph_erasure_code_corpus    2d7d78b9cc52e8a9529d8cc2d2954c7d375d5dd7
%global sub_blake3                      92e4cd71be48fdf9a79e88ef37b8f415ec5ac210
%global sub_arrow                       6a2e19a852b367c72d7b12da4d104456491ed8b7
%global sub_blkin                       f24ceec055ea236a093988237a9821d145f5f7c8
%global sub_c_ares                      fd6124c74da0801f23f9d324559d8b66fb83f533
%global sub_isa_l_crypto                a6dc869666fca3eef9a0305b290e4e0fc8bac645
%global sub_gf_complete                 7e61b44404f0ed410c83cfd3947a52e88ae044e1
%global sub_jerasure                    96c76b89d661c163f65a014b8042c9354ccf7f31
%global sub_fmt                         123913715afeb8a437e6388b4473fcc4753e1c9a
%global sub_googletest                  6910c9d9165801d8827d628cb72eb7ea9dd538c5
%global sub_isa_l                       bee5180a1517f8b5e70b02fcd66790c623536c5d
%global sub_opentelemetry_cpp           95fe422d56d74ded3640c5cdcaa3011bc9e18f68
%global sub_libkmip                     c05329f82a1a0e6d9bc4bae6fb25ce3d8e733f6c
%global sub_rook_client_python          82673cd7c7a3f4919b98706985ff27e57d2c1b94
%global sub_rocksdb                     24ea35870fe9b3ba15285ec8746ba97ed5d67ff3
%global sub_s3select                    0a0f6d439441f5b121ed1052dac54542e4f1d89b
# Nested submodules under src/s3select (ceph/s3select itself uses recursive
# submodules). Both are referenced unconditionally by the s3select include
# chain pulled in from src/rgw/rgw_s3select_private.h:
#   include/s3select_csv_parser.h -> #include "csvparser/csv.h"
#   src/CMakeLists.txt:417-421    -> s3select/rapidjson/include
%global sub_s3select_csvparser          5a417973b4cea674a5e4a3b88a23098a2ab75479
%global sub_s3select_rapidjson          fcb23c2dbf561ec0798529be4f66394d3e4996d8
%global sub_seastar                     15b1ca1bec7e148df262343f57b160d0248c736b
%global sub_utf8proc                    d7bf128df773c2a1a7242eb80e51e91a769fc985
%global sub_xxhash                      bbb27a5efb85b92a0486cf361a8635715a53f6ba
# Boost is not a submodule; make-dist downloads 1.87.0 and concatenates the
# tarball into the official release.
%global boost_version       1.87.0
%global boost_underscore    1_87_0

Name:           ceph
Version:        21.0.0
Release:        %autorelease
Summary:        User space components of the Ceph file system
License:        LGPL-2.1-or-later AND LGPL-3.0-only AND CC-BY-SA-3.0 AND GPL-2.0-only AND BSL-1.0 AND BSD-2-Clause AND BSD-3-Clause AND MIT
URL:            http://ceph.com/
VCS:            git:https://github.com/ceph/ceph
# GitHub archive tarball contains empty submodule placeholder dirs only.
# download.ceph.com release tarball (which bundles all submodules + boost)
# does not have v21.0.0 yet, so we reassemble from per-submodule archives below.
#!RemoteAsset:  sha256:321f745b69bce0a4a9f78fe708d8c6a523ea249c07dde5f11cfa6f515565caca
Source0:        https://github.com/ceph/ceph/archive/refs/tags/v%{version}.tar.gz#/ceph-%{version}.tar.gz
# Bundled isa-l v2.29 has no riscv64 support; v2.32.0 onwards ships
# riscv64 RVV sources. Used only on riscv64 to replace src/isa-l after
# the Source20 (submodule) extraction.
#!RemoteAsset:  sha256:7a194ff80d0f7e20615c497654e8a51b0184d0c79e2e265c7f555f52a26a05a4
Source1:        https://github.com/intel/isa-l/archive/refs/tags/v2.32.0.tar.gz#/isa-l-2.32.0.tar.gz
# https://github.com/intel/isa-l/pull/412
Source2:        isa-l-riscv64-rvv-raid-aliasing.patch
%if %{without system_boost}
#!RemoteAsset:  sha256:af57be25cb4c4f4b413ed692fe378affb4352ea50fbe294a11ef548f4d527d89
Source3:        https://archives.boost.io/release/%{boost_version}/source/boost_%{boost_underscore}.tar.bz2
%endif

# Submodule archives.
#!RemoteAsset:  sha256:f176d956c6eb862c3b10563e476f5ef9b7c3ad2b057ebe5c139ed6c31b84d236
Source10:       https://github.com/ceph/ceph-object-corpus/archive/%{sub_ceph_object_corpus}.tar.gz#/ceph-object-corpus-%{sub_ceph_object_corpus}.tar.gz
#!RemoteAsset:  sha256:842ac0500fcfd4e76045474abbe9079f8d54e7837cb2399d134929a0af281497
Source11:       https://github.com/ceph/ceph-erasure-code-corpus/archive/%{sub_ceph_erasure_code_corpus}.tar.gz#/ceph-erasure-code-corpus-%{sub_ceph_erasure_code_corpus}.tar.gz
#!RemoteAsset:  sha256:88930a1b7f3f910eda85219d29197611ee8ef468b9617285233af885eab86533
Source12:       https://github.com/BLAKE3-team/BLAKE3/archive/%{sub_blake3}.tar.gz#/BLAKE3-%{sub_blake3}.tar.gz
#!RemoteAsset:  sha256:03fe1b971609bdec287c77a5c9c89928a32be19875cb1458c711c1b80e33a7b4
Source13:       https://github.com/apache/arrow/archive/%{sub_arrow}.tar.gz#/arrow-%{sub_arrow}.tar.gz
#!RemoteAsset:  sha256:0bc468fddd8d77c354ab9e04899d7333b8c0543616f37bec383634c8ed7e87cc
Source14:       https://github.com/ceph/blkin/archive/%{sub_blkin}.tar.gz#/blkin-%{sub_blkin}.tar.gz
#!RemoteAsset:  sha256:8b76222d7bf9b35a1ed8194c65ac60b55a1b1ef0c2fb2a735e18bf1f387133b7
Source15:       https://github.com/ceph/c-ares/archive/%{sub_c_ares}.tar.gz#/c-ares-%{sub_c_ares}.tar.gz
#!RemoteAsset:  sha256:ebe7899b2494eb3f6cd3c7555cd970c2c9611e7ae5471f3fd41afd080bdf78fa
Source16:       https://github.com/intel/isa-l_crypto/archive/%{sub_isa_l_crypto}.tar.gz#/isa-l_crypto-%{sub_isa_l_crypto}.tar.gz
#!RemoteAsset:  sha256:8ff04510527262fbc741d9d84b1c9c6066e1dd909b3d5d37dc33dde27b0bc749
Source17:       https://github.com/ceph/gf-complete/archive/%{sub_gf_complete}.tar.gz#/gf-complete-%{sub_gf_complete}.tar.gz
#!RemoteAsset:  sha256:d6c24102341e7ec40cc63925e3a8b53a39bff088c8c04f166991f69bd954457c
Source18:       https://github.com/ceph/jerasure/archive/%{sub_jerasure}.tar.gz#/jerasure-%{sub_jerasure}.tar.gz
#!RemoteAsset:  sha256:95f89f1eb3b53478417185afc0b7e3d40ec889687af86e890da20068534d29f7
Source19:       https://github.com/ceph/fmt/archive/%{sub_fmt}.tar.gz#/fmt-%{sub_fmt}.tar.gz
#!RemoteAsset:  sha256:bde221be7f3841fcbc3971665d77d717116394a42155d988ee6407dfc39f1f09
Source20:       https://github.com/ceph/googletest/archive/%{sub_googletest}.tar.gz#/googletest-%{sub_googletest}.tar.gz
#!RemoteAsset:  sha256:569dd67a430d33400a147177b4e8d970a353d5528bfafd57da08f1bcffa50c25
Source21:       https://github.com/ceph/isa-l/archive/%{sub_isa_l}.tar.gz#/isa-l-bundled-%{sub_isa_l}.tar.gz
#!RemoteAsset:  sha256:4b20033029eb4e732f44428905ed71d024a3062e6936ce8112fc1bac8ef287e6
Source22:       https://github.com/ceph/opentelemetry-cpp/archive/%{sub_opentelemetry_cpp}.tar.gz#/opentelemetry-cpp-%{sub_opentelemetry_cpp}.tar.gz
#!RemoteAsset:  sha256:c272bf8545a8fe9c00af27f5d60e3f5b2955cae930738ab94b016f665bcb207a
Source23:       https://github.com/ceph/libkmip/archive/%{sub_libkmip}.tar.gz#/libkmip-%{sub_libkmip}.tar.gz
#!RemoteAsset:  sha256:bb6997295a967ac71e2e84a2d629d7828bdb056ffa427a57f925cf027b1a1974
Source24:       https://github.com/ceph/rook-client-python/archive/%{sub_rook_client_python}.tar.gz#/rook-client-python-%{sub_rook_client_python}.tar.gz
#!RemoteAsset:  sha256:323c630aaf76a02ff0ed4bcc5b34e100d34d286ce0ac21b90a267c165e1b4667
Source25:       https://github.com/ceph/rocksdb/archive/%{sub_rocksdb}.tar.gz#/rocksdb-%{sub_rocksdb}.tar.gz
#!RemoteAsset:  sha256:799b442ff8f7b03111fdd8bd43b07cb9a497fa384332b1acdd6c9a2bfd21206c
Source26:       https://github.com/ceph/s3select/archive/%{sub_s3select}.tar.gz#/s3select-%{sub_s3select}.tar.gz
#!RemoteAsset:  sha256:ab14ab9c9d8d715779b15a8c17a8c88aebd293b6be03ddfef97e4559a67acc53
Source27:       https://github.com/ceph/seastar/archive/%{sub_seastar}.tar.gz#/seastar-%{sub_seastar}.tar.gz
#!RemoteAsset:  sha256:9131e0a9c6fc25b0fe5d164a4e3eef1218bf22db33bd6b10bc43dc252d769afe
Source29:       https://github.com/JuliaStrings/utf8proc/archive/%{sub_utf8proc}.tar.gz#/utf8proc-%{sub_utf8proc}.tar.gz
#!RemoteAsset:  sha256:716fbe4fc85ecd36488afbbc635b59b5ab6aba5ed3b69d4a32a46eae5a453d38
Source30:       https://github.com/ceph/xxHash/archive/%{sub_xxhash}.tar.gz#/xxHash-%{sub_xxhash}.tar.gz
# Nested submodules of ceph/s3select (the s3select tarball itself ships empty
# submodule placeholders for these two; both are unconditionally pulled in by
# the s3select include chain used by src/rgw).
#!RemoteAsset:  sha256:daa7698f7c97a2ec7f4b78ee8466146668315506611d9d98c41e032a7aa9eb1b
Source32:       https://github.com/ben-strasser/fast-cpp-csv-parser/archive/%{sub_s3select_csvparser}.tar.gz#/fast-cpp-csv-parser-%{sub_s3select_csvparser}.tar.gz
#!RemoteAsset:  sha256:ced53d8e21e06b50a75e88b6bf8e2ef8ac1a21e2f30121a57b406648d247df4c
Source33:       https://github.com/Tencent/rapidjson/archive/%{sub_s3select_rapidjson}.tar.gz#/rapidjson-%{sub_s3select_rapidjson}.tar.gz
# Skipped submodules (not required by the current build options):
#   src/breakpad        (WITH_BREAKPAD=OFF below)
#   src/lss             (transitive dep of breakpad)
#   src/qatlib          (WITH_QATLIB=OFF)
#   src/qatzip          (WITH_QATZIP=OFF)
#   src/nvmeof/gateway  (only needed for nvmeof gateway client builds)
# Also skipped: nested submodules of the populated tarballs above. Their
# parent's build does not reference them under the current bcond set, but if
# the matching option is ever turned on the corresponding nested archive(s)
# must be added (mirroring src/s3select above):
#   src/spdk/{dpdk,intel-ipsec-mb,isa-l,ocf}                (needs WITH_SPDK)
#   src/seastar/dpdk                                        (needs WITH_CRIMSON + Seastar_DPDK)
#   src/arrow/{cpp/submodules/parquet-testing,testing}      (needs WITH_RADOSGW_SELECT_PARQUET)
#   src/jaegertracing/opentelemetry-cpp/third_party/nlohmann-json
#                                                           (needs OTLP/ZIPKIN/ELASTICSEARCH/ZPAGES/ETW exporter)
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
%if %{with spdk}
BuildOption(conf):  -DWITH_SPDK:BOOL=ON
BuildOption(conf):  -DWITH_SYSTEM_SPDK:BOOL=ON
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
# v21 wires Catch2 via CPM/FetchContent; WITH_SYSTEM_CATCH2=ON makes CPM resolve via find_package() against the system Catch2-devel.
BuildOption(conf):  -DWITH_SYSTEM_CATCH2:BOOL=ON
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
%if %{with system_boost}
BuildOption(conf):  -DWITH_SYSTEM_BOOST:BOOL=ON
%else
BuildOption(conf):  -DWITH_SYSTEM_BOOST:BOOL=OFF
%endif
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
# BOOST_J only drives the bundled-Boost b2 build; irrelevant with system Boost.
%if %{without system_boost}
BuildOption(conf):  -DBOOST_J:STRING=%{_smp_build_ncpus}
%endif
BuildOption(conf):  -Dxsimd_SOURCE="SYSTEM"
BuildOption(conf):  -DWITH_SYSTEM_UTF8PROC:BOOL=ON
BuildOption(conf):  -DWITH_QATDRV:BOOL=OFF
BuildOption(conf):  -DWITH_QATLIB:BOOL=OFF
BuildOption(conf):  -DWITH_QATZIP:BOOL=OFF
BuildOption(conf):  -DWITH_GRAFANA:BOOL=ON
BuildOption(conf):  -DCEPHADM_BUNDLED_DEPENDENCIES=none
# src/breakpad submodule intentionally not shipped; disable to avoid touching it.
BuildOption(conf):  -DWITH_BREAKPAD:BOOL=OFF
%if %{with crimson}
BuildOption(conf):  -DWITH_CRIMSON:BOOL=ON
%if %{with seastar_dpdk}
# Seastar DPDK network backend (src/seastar/dpdk).
BuildOption(conf):  -DSeastar_DPDK:BOOL=ON
%ifarch riscv64
BuildOption(conf):  -DSeastar_DPDK_MACHINE=rv64gcv
%endif
%endif
# Crimson and Jaeger tracing don't coexist (upstream ceph.spec.in forces
# WITH_JAEGER=OFF whenever WITH_CRIMSON=ON); override any prior ON above.
BuildOption(conf):  -DWITH_JAEGER:BOOL=OFF
%else
BuildOption(conf):  -DWITH_CRIMSON:BOOL=OFF
%endif

BuildRequires:  pkgconfig(libzstd)
BuildRequires:  gperf
BuildRequires:  cmake
%if %{with ceph_test_package}
# v21 wires Catch2 as a CPM/FetchContent dep for test binaries; system
# Catch2-devel is resolved via -DWITH_SYSTEM_CATCH2:BOOL=ON above.
BuildRequires:  cmake(Catch2)
%endif
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
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(cython)
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
%if %{with crimson}
# Bundled Seastar build-time deps (src/seastar). Ceph's WITH_CRIMSON wires
# in src/seastar; these are Seastar's own configure-time requirements,
# matched against upstream ceph.spec.in's "with crimson" block.
BuildRequires:  pkgconfig(libcares)
BuildRequires:  pkgconfig(hwloc)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libsctp)
BuildRequires:  pkgconfig(pciaccess)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(valgrind)
BuildRequires:  pkgconfig(yaml-cpp)
BuildRequires:  systemtap-sdt-devel
BuildRequires:  ragel
%if %{with seastar_dpdk}
BuildRequires:  pkgconfig(libdpdk)
%endif
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
%if %{with spdk}
# libdpdk: spdk_env_dpdk.pc Requires it. libisal: spdk's .so leave ISA-L symbols
# undefined for the final link and don't Require isa-l
BuildRequires:  pkgconfig(spdk_nvme)
BuildRequires:  pkgconfig(libdpdk)
BuildRequires:  pkgconfig(libisal)
%endif
%if %{with lttng}
BuildRequires:  pkgconfig(lttng-ust)
BuildRequires:  pkgconfig(babeltrace)
%endif
BuildRequires:  ninja
BuildRequires:  pkgconfig(ldap)
BuildRequires:  pkgconfig(numa)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  python3dist(prettytable)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(expat)
%if %{with system_boost}
# ceph 21 hard-requires Boost 1.87 (CMakeLists.txt: find_package(Boost 1.87 REQUIRED)).
BuildRequires:  boost-devel
%endif
BuildRequires:  python-rpm-macros
%if %{with make_check}
# run-tox-mgr venv builds scipy from sdist (no riscv64 wheel): gcc-fortran + OpenBLAS.
BuildRequires:  gcc-fortran
# jsonnet-bundler-build.sh: go build at test time.
BuildRequires:  git
BuildRequires:  go
# unittest_hostname / unittest_config exec("hostname")
BuildRequires:  hostname
# src/test/cli/crushtool/choose-args.t pipes crushtool --dump into jq.
BuildRequires:  jq
# monitoring/ceph-mixin/lint-jsonnet.sh invokes jsonnet directly.
BuildRequires:  jsonnet
# scipy sdist; see gcc-fortran comment above.
BuildRequires:  pkgconfig(openblas)
# run-tox-alerts-{lint,check} invoke promtool.
BuildRequires:  promtool
# cryptography sdist; see gcc-fortran comment above.
BuildRequires:  rust
%endif

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
# https://github.com/ceph/ceph/commit/3ccfff1acd6fa5babc7de035271b7f91fccabb8c
1001-arch-riscv-fix-hwprobe.patch
# https://github.com/ceph/ceph/commit/c82cd26ac4c64f7b307d5630a5bfb2204a8dc3b8
1002-test-crimson-fix-test-remap-pin-concurrent.patch
# https://github.com/ceph/ceph/commit/980177003c23fda412e07afa84524b5e990f9b8c
1003-test-crimson-object-data-handler-init-known-contents.patch
# https://github.com/ceph/ceph/pull/69156
1004-monitoring-ceph-mixin-jsonnet-bundler-version.patch
# https://github.com/ceph/ceph/pull/69157
1005-test-mds-quiesce-agent-evaluate-await-idle.patch
# https://github.com/ceph/ceph/commit/fbcd8a4a37e02a67a29928160cfe79be116a94aa
1006-isa-l-enable-on-riscv.patch
# https://github.com/ceph/ceph/pull/69161
1007-librbd-pwl-cancel-timer-before-perf-stop.patch
# https://github.com/ceph/ceph/pull/69162
1008-cephadm-tests-mock-find-program-lvcreate.patch
# https://github.com/ceph/ceph/commit/82ff35794af071654368347426879519f3aff266
1009-crimson-seastore-record-submitter-wait-available-idempotent.patch
# https://github.com/ceph/ceph/pull/69165
1010-cmake-AddCephTest-use-catch2-imported-target.patch
# https://github.com/ceph/ceph/commit/868fdd8120790ef453692604fff910e29c56cee1
1011-rgw-rest-swift-error-handler-out-of-line.patch
# https://github.com/scylladb/seastar/commit/59225b1c6d2225b67dd2f2cebd3aa22be84b55d3
1012-src-seastar-add-initial-riscv-port.patch
# https://github.com/scylladb/seastar/pull/3435
1013-seastar-io-uring-retry-socket-send-on-eagain.patch
# https://github.com/ceph/ceph/commit/d18ffa868fde6af02548404d95c7c0fe8947ddc6
1014-blk-spdk-support-both-old-and-new-spdk_env_opts-memb.patch
# https://github.com/ceph/ceph/commit/6af1a859468c2cf9697e23fb428b24f49fe74e74
1015-cmake-add-WITH_SYSTEM_SPDK-to-link-a-system-installe.patch
# https://github.com/scylladb/seastar/pull/3436
1016-cmake-don-t-require-i40e-sfc-DPDK-PMDs-on-RISC-V.patch
# https://github.com/scylladb/seastar/pull/3437
1017-build-also-detect-GCC-s-Wno-error-cpp-for-warning.patch
# https://github.com/ceph/ceph/pull/69187
1018-cmake-rename-Finddpdk-module-to-FindDPDK.patch
# https://github.com/ceph/ceph/pull/69188
1019-compressor-zstd-include-zstd.h-instead-of-the-bundle.patch
# https://github.com/ceph/ceph/pull/69215
1020-build-link-legacy-option-headers-from-targets-racing.patch
# https://github.com/scylladb/seastar/pull/3441
1021-cmake-guard-DPDK-dpdk-against-redefinition-in-Finddp.patch

# Bump pylint 2.6.0 -> 2.17.7 for Python 3.13 / wrapt compat.
2001-monitoring-ceph-mixin-bump-pylint.patch
# Bump cephadm pyfakefs pin to >=5.7,<6 for Python 3.13.
2002-cephadm-tox-pyfakefs-py313.patch
# mgr tox: drop flake8 git ls-files refcount checks (no .git in tarball).
2003-mgr-tox-skip-git-ls-files.patch
# unittest-seastar-messenger-thrash --memory 256M -> 1G (too tight on riscv64).
2004-test-crimson-messenger-thrash-bump-memory.patch
# memstore STATIC: avoid os<->memstore cycle under BUILD_SHARED_LIBS=ON.
2005-os-memstore-static.patch
# dbstore_lib STATIC + link global: avoid SHARED cycle under BUILD_SHARED_LIBS=ON.
2006-src-rgw-store-dbstore-CMakeLists.txt.patch
# cephadm tox: drop flake8 git ls-files registry assertions (no .git in tarball).
2007-cephadm-tox-drop-git-lsfiles-checks.patch

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

%if %{with crimson}
%package        crimson-osd
Summary:        Ceph Object Storage Daemon, Crimson implementation
Requires:       ceph-osd%{?_isa} = %{version}-%{release}
Requires:       binutils

%description    crimson-osd
crimson-osd is the next-generation Ceph object storage daemon, built on
the Seastar shared-nothing framework for low-latency NVMe back ends. It
shares on-disk format and tooling with the classic ceph-osd but runs
each shard pinned to a single core with user-space polled I/O.
%endif

%package        osd
Summary:        Ceph Object Storage Daemon
Requires:       ceph-base%{?_isa} = %{version}-%{release}
Requires:       sudo
Requires:       libstoragemgmt
%if %{with crimson}
# crimson links against the system protobuf shared library at runtime.
Requires:       protobuf
%endif
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

%prep
# Fully override the BuildSystem-injected prep stage: numbered patches must be
# applied AFTER the submodule tarballs are extracted, because
# 1012-src-seastar-add-initial-riscv-port touches files under src/seastar/ -
# which is an empty placeholder dir until SOURCE27 is extracted below.
%autosetup -p1 -N
# GitHub archive tarball ships empty submodule placeholder dirs.
# Populate each from its pinned-SHA archive Source.
tar -xf %{SOURCE10} -C ceph-object-corpus            --strip-components=1
tar -xf %{SOURCE11} -C ceph-erasure-code-corpus      --strip-components=1
tar -xf %{SOURCE12} -C src/BLAKE3                    --strip-components=1
tar -xf %{SOURCE13} -C src/arrow                     --strip-components=1
tar -xf %{SOURCE14} -C src/blkin                     --strip-components=1
tar -xf %{SOURCE15} -C src/c-ares                    --strip-components=1
tar -xf %{SOURCE16} -C src/crypto/isa-l/isa-l_crypto --strip-components=1
tar -xf %{SOURCE17} -C src/erasure-code/jerasure/gf-complete --strip-components=1
tar -xf %{SOURCE18} -C src/erasure-code/jerasure/jerasure   --strip-components=1
tar -xf %{SOURCE19} -C src/fmt                       --strip-components=1
tar -xf %{SOURCE20} -C src/googletest                --strip-components=1
tar -xf %{SOURCE21} -C src/isa-l                     --strip-components=1
tar -xf %{SOURCE22} -C src/jaegertracing/opentelemetry-cpp --strip-components=1
tar -xf %{SOURCE23} -C src/libkmip                   --strip-components=1
tar -xf %{SOURCE24} -C src/pybind/mgr/rook/rook-client-python --strip-components=1
tar -xf %{SOURCE25} -C src/rocksdb                   --strip-components=1
tar -xf %{SOURCE26} -C src/s3select                  --strip-components=1
tar -xf %{SOURCE27} -C src/seastar                   --strip-components=1
tar -xf %{SOURCE29} -C src/utf8proc                  --strip-components=1
tar -xf %{SOURCE30} -C src/xxHash                    --strip-components=1
# Nested submodules under src/s3select. The s3select tarball ships its
# include/csvparser and rapidjson dirs as empty submodule placeholders;
# populate them after Source26 extraction above.
tar -xf %{SOURCE32} -C src/s3select/include/csvparser --strip-components=1
tar -xf %{SOURCE33} -C src/s3select/rapidjson         --strip-components=1

# Boost (cmake BuildBoost.cmake expects src/boost/boost/version.hpp).
%if %{without system_boost}
tar -xf %{SOURCE3} -C src
mv src/boost_%{boost_underscore} src/boost
%endif

# Replace bundled isa-l (v2.x submodule head) with v2.32.0 only on riscv64:
# v2.32+ ships the riscv64 RVV sources we need. Done AFTER the submodule
# population above so we are overwriting a known state.
%ifarch riscv64
rm -rf src/isa-l
tar -xf %{SOURCE1} -C src
mv src/isa-l-2.32.0 src/isa-l

patch -p1 -i %{SOURCE2}
%endif

# Apply numbered patches now that all submodule placeholders (src/seastar,
# src/isa-l, etc.) are populated; see the autosetup -N call above.
%autopatch -p1

# src/CMakeLists.txt reads src/.git_version when .git/ is absent (true for
# GitHub archive tarballs; the file is only generated by upstream make-dist).
# Provide a placeholder so %conf can proceed; the values only feed the
# embedded version string.
printf '%s\n%s\n' 0000000000000000000000000000000000000000 v%{version} > src/.git_version

# Create two sysusers.d config files
cat >ceph.sysusers.conf <<EOF
g ceph 167
u ceph 167 'Ceph storage service' %{_localstatedir}/lib/ceph -
EOF
cat >cephadm.sysusers.conf <<EOF
u cephadm - 'cephadm user for mgr/cephadm' %{_sharedstatedir}/cephadm /bin/bash
EOF

%check
%if %{with make_check}
# unittest_* targets are EXCLUDE_FROM_ALL; build the `tests` aggregate before ctest.
%cmake_build --target tests
# Stale golden PromQL values pinned to an older prometheus
%ctest -E '^(run-tox-promql-query-test|run-promtool-unittests)$'
%endif

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
%{_datadir}/ceph/mgr/cherrypy_mgr.py
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
%{_datadir}/ceph/mgr/nvmeof
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

%if %{with crimson}
%files crimson-osd
%{_bindir}/crimson-osd
%endif

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
%{_includedir}/cephfs/dump.h
%{_includedir}/cephfs/json.h
%{_includedir}/cephfs/keys_and_values.h
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
%{python3_sitearch}/rados-*.dist-info

%files -n python-rgw
%{python3_sitearch}/rgw.cpython*.so
%{python3_sitearch}/rgw-*.dist-info

%files -n python-rbd
%{python3_sitearch}/rbd.cpython*.so
%{python3_sitearch}/rbd-*.dist-info

%files -n python-cephfs
%{python3_sitearch}/cephfs.cpython*.so
%{python3_sitearch}/cephfs-*.dist-info

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
%{_bindir}/ceph_ec_consistency_checker
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
%if %{with crimson}
%{_bindir}/crimson-objectstore-tool
%{_bindir}/crimson-store-bench
%{_bindir}/crimson-store-nbd
%endif
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
