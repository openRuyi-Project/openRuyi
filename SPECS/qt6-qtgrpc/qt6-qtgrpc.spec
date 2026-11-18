# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt_module qtgrpc
%define short_version 6.12

Name:           qt6-qtgrpc
Version:        6.12.0
Release:        %autorelease
Summary:        Qt6 - Support for using gRPC and Protobuf
License:        GPL-3.0-only AND (LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only) AND (GPL-3.0-only WITH Qt-GPL-exception-1.0) AND BSD-3-Clause AND Apache-2.0
URL:            https://www.qt.io
VCS:            git:https://github.com/qt/qtgrpc
#!RemoteAsset:  sha256:771852c4e5fbeb3d7c3b2a9aacc13db9efe942a46e7d1454ec1f16092ec3ef9c
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz
BuildSystem:    cmake

# Install the magic8ball example plugin; https://github.com/qt/qtgrpc/blob/v6.12.0/examples/grpc/magic8ball/CMakeLists.txt.
Patch0:         2000-install-magic8ball-plugin.patch

BuildOption(conf):  -GNinja
BuildOption(conf):  -DQT_BUILD_EXAMPLES:BOOL=ON
BuildOption(conf):  -DQT_INSTALL_EXAMPLES_SOURCES:BOOL=ON

BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  gcc-c++
BuildRequires:  qt6-macros
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  pkgconfig(Qt6Quick) >= %{version}
BuildRequires:  pkgconfig(grpc++)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(zlib)

%description
Protocol Buffers (Protobuf) is a cross-platform data format used to
serialize structured data. gRPC provides a remote procedure call
framework based on Protobuf. Qt provides tooling and classes to
use these technologies.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(Qt6Network)
Requires:       pkgconfig(protobuf)

%description    devel
Development files for %{name}.

%package        examples
Summary:        Programming examples for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    examples
Programming examples for %{name}.

%files
%license LICENSES/*
%{_qt6_libdir}/libQt6Grpc.so.6*
%{_qt6_libdir}/libQt6Protobuf.so.6*
%{_qt6_libdir}/libQt6ProtobufQtCoreTypes.so.6*
%{_qt6_libdir}/libQt6ProtobufQtGuiTypes.so.6*
%{_qt6_libdir}/libQt6ProtobufWellKnownTypes.so.6*
%{_qt6_libdir}/libQt6GrpcQuick.so.6*
%{_qt6_libdir}/libQt6ProtobufQuick.so.6*
%{_qt6_qmldir}/QtGrpc/
%{_qt6_qmldir}/QtProtobuf/
%{_qt6_archdatadir}/sbom/%{qt_module}-%{version}.spdx

%files devel
%{_qt6_includedir}/QtGrpc/
%{_qt6_includedir}/QtProtobuf/
%{_qt6_includedir}/QtProtobufQtCoreTypes/
%{_qt6_includedir}/QtProtobufQtGuiTypes/
%{_qt6_includedir}/QtProtobufWellKnownTypes/
%{_qt6_includedir}/QtGrpcQuick/
%{_qt6_includedir}/QtProtobufQuick/
%{_qt6_libdir}/libQt6Grpc.so
%{_qt6_libdir}/libQt6Protobuf.so
%{_qt6_libdir}/libQt6ProtobufQtCoreTypes.so
%{_qt6_libdir}/libQt6ProtobufQtGuiTypes.so
%{_qt6_libdir}/libQt6ProtobufWellKnownTypes.so
%{_qt6_libdir}/libQt6Grpc.prl
%{_qt6_libdir}/libQt6Protobuf.prl
%{_qt6_libdir}/libQt6ProtobufWellKnownTypes.prl
%{_qt6_libdir}/libQt6ProtobufQtCoreTypes.prl
%{_qt6_libdir}/libQt6ProtobufQtGuiTypes.prl
%{_qt6_libdir}/libQt6GrpcQuick.so
%{_qt6_libdir}/libQt6GrpcQuick.prl
%{_qt6_libdir}/libQt6ProtobufQuick.so
%{_qt6_libdir}/libQt6ProtobufQuick.prl
%{_qt6_libdir}/cmake/Qt6Grpc/
%{_qt6_libdir}/cmake/Qt6GrpcPrivate/
%{_qt6_libdir}/cmake/Qt6GrpcQuick/
%{_qt6_libdir}/cmake/Qt6GrpcQuickPrivate/
%{_qt6_libdir}/cmake/Qt6GrpcTools/
%{_qt6_libdir}/cmake/Qt6Protobuf/
%{_qt6_libdir}/cmake/Qt6ProtobufPrivate/
%{_qt6_libdir}/cmake/Qt6ProtobufQtCoreTypes/
%{_qt6_libdir}/cmake/Qt6ProtobufQtCoreTypesPrivate/
%{_qt6_libdir}/cmake/Qt6ProtobufQtGuiTypes/
%{_qt6_libdir}/cmake/Qt6ProtobufQtGuiTypesPrivate/
%{_qt6_libdir}/cmake/Qt6ProtobufQuick/
%{_qt6_libdir}/cmake/Qt6ProtobufQuickPrivate/
%{_qt6_libdir}/cmake/Qt6ProtobufTools/
%{_qt6_libdir}/cmake/Qt6ProtobufWellKnownTypes/
%{_qt6_libdir}/cmake/Qt6ProtobufWellKnownTypesPrivate/
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/
%{_qt6_libdir}/cmake/Qt6/*.cmake
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtGrpcTestsConfig.cmake
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_datadir}/modules/*.json
%{_qt6_libdir}/pkgconfig/Qt6Grpc.pc
%{_qt6_libdir}/pkgconfig/Qt6GrpcQuick.pc
%{_qt6_libdir}/pkgconfig/Qt6Protobuf.pc
%{_qt6_libdir}/pkgconfig/Qt6ProtobufQtCoreTypes.pc
%{_qt6_libdir}/pkgconfig/Qt6ProtobufQtGuiTypes.pc
%{_qt6_libdir}/pkgconfig/Qt6ProtobufQuick.pc
%{_qt6_libdir}/pkgconfig/Qt6ProtobufWellKnownTypes.pc
%{_qt6_libexecdir}/qtgrpcgen
%{_qt6_libexecdir}/qtprotobufgen

%files examples
%{_qt6_examplesdir}/

%changelog
%autochangelog
