# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name glow
%global full_version 0.16.0
%global pkgname glow-0.16

Name:           rust-glow-0.16
Version:        0.16.0
Release:        %autorelease
Summary:        Rust crate "glow"
License:        MIT OR Apache-2.0 OR Zlib
URL:            https://github.com/grovesNL/glow.git
#!RemoteAsset:  sha256:c5e5ea60d70410161c8bf5da3fdfeaa1c72ed2c15f8bbb9d19fe3a4fad085f08
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(js-sys-0.3/default) >= 0.3.0
Requires:       crate(slotmap-1/default) >= 1.0.0
Requires:       crate(wasm-bindgen-0.2/default) >= 0.2.0
Requires:       crate(web-sys-0.3/angleinstancedarrays) >= 0.3.60
Requires:       crate(web-sys-0.3/default) >= 0.3.60
Requires:       crate(web-sys-0.3/document) >= 0.3.60
Requires:       crate(web-sys-0.3/element) >= 0.3.60
Requires:       crate(web-sys-0.3/extblendminmax) >= 0.3.60
Requires:       crate(web-sys-0.3/extcolorbufferfloat) >= 0.3.60
Requires:       crate(web-sys-0.3/extcolorbufferhalffloat) >= 0.3.60
Requires:       crate(web-sys-0.3/extdisjointtimerquery) >= 0.3.60
Requires:       crate(web-sys-0.3/extfragdepth) >= 0.3.60
Requires:       crate(web-sys-0.3/extshadertexturelod) >= 0.3.60
Requires:       crate(web-sys-0.3/extsrgb) >= 0.3.60
Requires:       crate(web-sys-0.3/exttexturefilteranisotropic) >= 0.3.60
Requires:       crate(web-sys-0.3/htmlcanvaselement) >= 0.3.60
Requires:       crate(web-sys-0.3/htmlimageelement) >= 0.3.60
Requires:       crate(web-sys-0.3/htmlvideoelement) >= 0.3.60
Requires:       crate(web-sys-0.3/imagebitmap) >= 0.3.60
Requires:       crate(web-sys-0.3/imagedata) >= 0.3.60
Requires:       crate(web-sys-0.3/oeselementindexuint) >= 0.3.60
Requires:       crate(web-sys-0.3/oesstandardderivatives) >= 0.3.60
Requires:       crate(web-sys-0.3/oestexturefloat) >= 0.3.60
Requires:       crate(web-sys-0.3/oestexturefloatlinear) >= 0.3.60
Requires:       crate(web-sys-0.3/oestexturehalffloat) >= 0.3.60
Requires:       crate(web-sys-0.3/oestexturehalffloatlinear) >= 0.3.60
Requires:       crate(web-sys-0.3/oesvertexarrayobject) >= 0.3.60
Requires:       crate(web-sys-0.3/ovrmultiview2) >= 0.3.60
Requires:       crate(web-sys-0.3/videoframe) >= 0.3.60
Requires:       crate(web-sys-0.3/webgl2renderingcontext) >= 0.3.60
Requires:       crate(web-sys-0.3/webglactiveinfo) >= 0.3.60
Requires:       crate(web-sys-0.3/webglbuffer) >= 0.3.60
Requires:       crate(web-sys-0.3/webglcolorbufferfloat) >= 0.3.60
Requires:       crate(web-sys-0.3/webglcompressedtextureastc) >= 0.3.60
Requires:       crate(web-sys-0.3/webglcompressedtextureetc) >= 0.3.60
Requires:       crate(web-sys-0.3/webglcompressedtextureetc1) >= 0.3.60
Requires:       crate(web-sys-0.3/webglcompressedtexturepvrtc) >= 0.3.60
Requires:       crate(web-sys-0.3/webglcompressedtextures3tc) >= 0.3.60
Requires:       crate(web-sys-0.3/webglcompressedtextures3tcsrgb) >= 0.3.60
Requires:       crate(web-sys-0.3/webgldebugrendererinfo) >= 0.3.60
Requires:       crate(web-sys-0.3/webgldebugshaders) >= 0.3.60
Requires:       crate(web-sys-0.3/webgldepthtexture) >= 0.3.60
Requires:       crate(web-sys-0.3/webgldrawbuffers) >= 0.3.60
Requires:       crate(web-sys-0.3/webglframebuffer) >= 0.3.60
Requires:       crate(web-sys-0.3/webgllosecontext) >= 0.3.60
Requires:       crate(web-sys-0.3/webglprogram) >= 0.3.60
Requires:       crate(web-sys-0.3/webglquery) >= 0.3.60
Requires:       crate(web-sys-0.3/webglrenderbuffer) >= 0.3.60
Requires:       crate(web-sys-0.3/webglrenderingcontext) >= 0.3.60
Requires:       crate(web-sys-0.3/webglsampler) >= 0.3.60
Requires:       crate(web-sys-0.3/webglshader) >= 0.3.60
Requires:       crate(web-sys-0.3/webglshaderprecisionformat) >= 0.3.60
Requires:       crate(web-sys-0.3/webglsync) >= 0.3.60
Requires:       crate(web-sys-0.3/webgltexture) >= 0.3.60
Requires:       crate(web-sys-0.3/webgltransformfeedback) >= 0.3.60
Requires:       crate(web-sys-0.3/webgluniformlocation) >= 0.3.60
Requires:       crate(web-sys-0.3/webglvertexarrayobject) >= 0.3.60
Requires:       crate(web-sys-0.3/window) >= 0.3.60
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/debug-automatic-glgeterror) = %{version}
Provides:       crate(%{pkgname}/debug-trace-calls) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "glow"

%package     -n %{name}+log
Summary:        GL on Whatever: a set of bindings to run GL (Open GL, OpenGL ES, and WebGL) anywhere, and avoid target-specific code - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.16
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust glow crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
