# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name objc2-metal
%global full_version 0.2.2
%global pkgname objc2-metal-0.2

Name:           rust-objc2-metal-0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Rust crate "objc2-metal"
License:        MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:dd0cba1276f6023976a406a14ffa85e1fdd19df6b0f737b063b95f6c8c7aadd6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(objc2-0.5) >= 0.5.2
Requires:       crate(objc2-foundation-0.2) >= 0.2.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/mtlaccelerationstructuretypes) = %{version}
Provides:       crate(%{pkgname}/mtldefines) = %{version}
Provides:       crate(%{pkgname}/mtldrawable) = %{version}
Provides:       crate(%{pkgname}/mtlindirectcommandencoder) = %{version}
Provides:       crate(%{pkgname}/mtliocompressor) = %{version}
Provides:       crate(%{pkgname}/mtlparallelrendercommandencoder) = %{version}
Provides:       crate(%{pkgname}/mtlpixelformat) = %{version}
Provides:       crate(%{pkgname}/mtlresourcestatecommandencoder) = %{version}
Provides:       crate(%{pkgname}/mtltypes) = %{version}

%description
Source code for takopackized Rust crate "objc2-metal"

%package     -n %{name}+mtlaccelerationstructure
Summary:        Bindings to the Metal framework - feature "MTLAccelerationStructure" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/mtlaccelerationstructure) = %{version}
Provides:       crate(%{pkgname}/mtlfunctiondescriptor) = %{version}

%description -n %{name}+mtlaccelerationstructure
This metapackage enables feature "MTLAccelerationStructure" for the Rust objc2-metal crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "MTLFunctionDescriptor" feature.

%package     -n %{name}+mtlaccelerationstructurecommandencoder
Summary:        Bindings to the Metal framework - feature "MTLAccelerationStructureCommandEncoder" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Provides:       crate(%{pkgname}/mtlaccelerationstructurecommandencoder) = %{version}
Provides:       crate(%{pkgname}/mtlrenderpass) = %{version}

%description -n %{name}+mtlaccelerationstructurecommandencoder
This metapackage enables feature "MTLAccelerationStructureCommandEncoder" for the Rust objc2-metal crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "MTLRenderPass" feature.

%package     -n %{name}+mtlargument
Summary:        Bindings to the Metal framework - feature "MTLArgument"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/mtlargument) = %{version}

%description -n %{name}+mtlargument
This metapackage enables feature "MTLArgument" for the Rust objc2-metal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mtlargumentencoder
Summary:        Bindings to the Metal framework - feature "MTLArgumentEncoder" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsrange) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/mtlargumentencoder) = %{version}
Provides:       crate(%{pkgname}/mtlbuffer) = %{version}

%description -n %{name}+mtlargumentencoder
This metapackage enables feature "MTLArgumentEncoder" for the Rust objc2-metal crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "MTLBuffer" feature.

%package     -n %{name}+mtlbinaryarchive
Summary:        Bindings to the Metal framework - feature "MTLBinaryArchive" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/mtlbinaryarchive) = %{version}
Provides:       crate(%{pkgname}/mtlcapturemanager) = %{version}

%description -n %{name}+mtlbinaryarchive
This metapackage enables feature "MTLBinaryArchive" for the Rust objc2-metal crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "MTLCaptureManager" feature.

%package     -n %{name}+mtlblitcommandencoder
Summary:        Bindings to the Metal framework - feature "MTLBlitCommandEncoder" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsrange) >= 0.2.2
Provides:       crate(%{pkgname}/mtlblitcommandencoder) = %{version}
Provides:       crate(%{pkgname}/mtlrendercommandencoder) = %{version}

%description -n %{name}+mtlblitcommandencoder
This metapackage enables feature "MTLBlitCommandEncoder" for the Rust objc2-metal crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "MTLRenderCommandEncoder" feature.

%package     -n %{name}+mtlblitpass
Summary:        Bindings to the Metal framework - feature "MTLBlitPass" and 5 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Provides:       crate(%{pkgname}/mtlblitpass) = %{version}
Provides:       crate(%{pkgname}/mtlcomputepass) = %{version}
Provides:       crate(%{pkgname}/mtlpipeline) = %{version}
Provides:       crate(%{pkgname}/mtlresourcestatepass) = %{version}
Provides:       crate(%{pkgname}/mtlstageinputoutputdescriptor) = %{version}
Provides:       crate(%{pkgname}/mtlvertexdescriptor) = %{version}

%description -n %{name}+mtlblitpass
This metapackage enables feature "MTLBlitPass" for the Rust objc2-metal crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "MTLComputePass", "MTLPipeline", "MTLResourceStatePass", "MTLStageInputOutputDescriptor", and "MTLVertexDescriptor" features.

%package     -n %{name}+mtlcapturescope
Summary:        Bindings to the Metal framework - feature "MTLCaptureScope" and 3 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/mtlcapturescope) = %{version}
Provides:       crate(%{pkgname}/mtlcommandqueue) = %{version}
Provides:       crate(%{pkgname}/mtlfence) = %{version}
Provides:       crate(%{pkgname}/mtlfunctionhandle) = %{version}

%description -n %{name}+mtlcapturescope
This metapackage enables feature "MTLCaptureScope" for the Rust objc2-metal crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "MTLCommandQueue", "MTLFence", and "MTLFunctionHandle" features.

%package     -n %{name}+mtlcommandbuffer
Summary:        Bindings to the Metal framework - feature "MTLCommandBuffer"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsenumerator) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/mtlcommandbuffer) = %{version}

%description -n %{name}+mtlcommandbuffer
This metapackage enables feature "MTLCommandBuffer" for the Rust objc2-metal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mtlcommandencoder
Summary:        Bindings to the Metal framework - feature "MTLCommandEncoder" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/mtlcommandencoder) = %{version}
Provides:       crate(%{pkgname}/mtlresource) = %{version}

%description -n %{name}+mtlcommandencoder
This metapackage enables feature "MTLCommandEncoder" for the Rust objc2-metal crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "MTLResource" feature.

%package     -n %{name}+mtlcomputecommandencoder
Summary:        Bindings to the Metal framework - feature "MTLComputeCommandEncoder"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsrange) >= 0.2.2
Provides:       crate(%{pkgname}/mtlcomputecommandencoder) = %{version}

%description -n %{name}+mtlcomputecommandencoder
This metapackage enables feature "MTLComputeCommandEncoder" for the Rust objc2-metal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mtlcomputepipeline
Summary:        Bindings to the Metal framework - feature "MTLComputePipeline"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/mtlcomputepipeline) = %{version}

%description -n %{name}+mtlcomputepipeline
This metapackage enables feature "MTLComputePipeline" for the Rust objc2-metal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mtlcounters
Summary:        Bindings to the Metal framework - feature "MTLCounters"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsrange) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/mtlcounters) = %{version}

%description -n %{name}+mtlcounters
This metapackage enables feature "MTLCounters" for the Rust objc2-metal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mtldepthstencil
Summary:        Bindings to the Metal framework - feature "MTLDepthStencil" and 3 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/mtldepthstencil) = %{version}
Provides:       crate(%{pkgname}/mtlevent) = %{version}
Provides:       crate(%{pkgname}/mtlheap) = %{version}
Provides:       crate(%{pkgname}/mtlsampler) = %{version}

%description -n %{name}+mtldepthstencil
This metapackage enables feature "MTLDepthStencil" for the Rust objc2-metal crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "MTLEvent", "MTLHeap", and "MTLSampler" features.

%package     -n %{name}+mtldevice
Summary:        Bindings to the Metal framework - feature "MTLDevice"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsbundle) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/mtldevice) = %{version}

%description -n %{name}+mtldevice
This metapackage enables feature "MTLDevice" for the Rust objc2-metal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mtldynamiclibrary
Summary:        Bindings to the Metal framework - feature "MTLDynamicLibrary"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/mtldynamiclibrary) = %{version}

%description -n %{name}+mtldynamiclibrary
This metapackage enables feature "MTLDynamicLibrary" for the Rust objc2-metal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mtlfunctionconstantvalues
Summary:        Bindings to the Metal framework - feature "MTLFunctionConstantValues"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsrange) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/mtlfunctionconstantvalues) = %{version}

%description -n %{name}+mtlfunctionconstantvalues
This metapackage enables feature "MTLFunctionConstantValues" for the Rust objc2-metal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mtlfunctionlog
Summary:        Bindings to the Metal framework - feature "MTLFunctionLog"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsenumerator) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/mtlfunctionlog) = %{version}

%description -n %{name}+mtlfunctionlog
This metapackage enables feature "MTLFunctionLog" for the Rust objc2-metal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mtlfunctionstitching
Summary:        Bindings to the Metal framework - feature "MTLFunctionStitching"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/mtlfunctionstitching) = %{version}

%description -n %{name}+mtlfunctionstitching
This metapackage enables feature "MTLFunctionStitching" for the Rust objc2-metal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mtliocommandbuffer
Summary:        Bindings to the Metal framework - feature "MTLIOCommandBuffer"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/mtliocommandbuffer) = %{version}

%description -n %{name}+mtliocommandbuffer
This metapackage enables feature "MTLIOCommandBuffer" for the Rust objc2-metal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mtliocommandqueue
Summary:        Bindings to the Metal framework - feature "MTLIOCommandQueue"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/mtliocommandqueue) = %{version}

%description -n %{name}+mtliocommandqueue
This metapackage enables feature "MTLIOCommandQueue" for the Rust objc2-metal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mtlindirectcommandbuffer
Summary:        Bindings to the Metal framework - feature "MTLIndirectCommandBuffer" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsrange) >= 0.2.2
Provides:       crate(%{pkgname}/mtlindirectcommandbuffer) = %{version}
Provides:       crate(%{pkgname}/mtlintersectionfunctiontable) = %{version}

%description -n %{name}+mtlindirectcommandbuffer
This metapackage enables feature "MTLIndirectCommandBuffer" for the Rust objc2-metal crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "MTLIntersectionFunctionTable" feature.

%package     -n %{name}+mtllibrary
Summary:        Bindings to the Metal framework - feature "MTLLibrary"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/mtllibrary) = %{version}

%description -n %{name}+mtllibrary
This metapackage enables feature "MTLLibrary" for the Rust objc2-metal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mtllinkedfunctions
Summary:        Bindings to the Metal framework - feature "MTLLinkedFunctions"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/mtllinkedfunctions) = %{version}

%description -n %{name}+mtllinkedfunctions
This metapackage enables feature "MTLLinkedFunctions" for the Rust objc2-metal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mtlrasterizationrate
Summary:        Bindings to the Metal framework - feature "MTLRasterizationRate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsvalue) >= 0.2.2
Provides:       crate(%{pkgname}/mtlrasterizationrate) = %{version}

%description -n %{name}+mtlrasterizationrate
This metapackage enables feature "MTLRasterizationRate" for the Rust objc2-metal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mtlrenderpipeline
Summary:        Bindings to the Metal framework - feature "MTLRenderPipeline"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/mtlrenderpipeline) = %{version}

%description -n %{name}+mtlrenderpipeline
This metapackage enables feature "MTLRenderPipeline" for the Rust objc2-metal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mtltexture
Summary:        Bindings to the Metal framework - feature "MTLTexture"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsrange) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/mtltexture) = %{version}

%description -n %{name}+mtltexture
This metapackage enables feature "MTLTexture" for the Rust objc2-metal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mtlvisiblefunctiontable
Summary:        Bindings to the Metal framework - feature "MTLVisibleFunctionTable"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsrange) >= 0.2.2
Provides:       crate(%{pkgname}/mtlvisiblefunctiontable) = %{version}

%description -n %{name}+mtlvisiblefunctiontable
This metapackage enables feature "MTLVisibleFunctionTable" for the Rust objc2-metal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+all
Summary:        Bindings to the Metal framework - feature "all"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(%{pkgname}/block2) = %{version}
Requires:       crate(%{pkgname}/mtlaccelerationstructure) = %{version}
Requires:       crate(%{pkgname}/mtlaccelerationstructurecommandencoder) = %{version}
Requires:       crate(%{pkgname}/mtlaccelerationstructuretypes) = %{version}
Requires:       crate(%{pkgname}/mtlargument) = %{version}
Requires:       crate(%{pkgname}/mtlargumentencoder) = %{version}
Requires:       crate(%{pkgname}/mtlbinaryarchive) = %{version}
Requires:       crate(%{pkgname}/mtlblitcommandencoder) = %{version}
Requires:       crate(%{pkgname}/mtlblitpass) = %{version}
Requires:       crate(%{pkgname}/mtlbuffer) = %{version}
Requires:       crate(%{pkgname}/mtlcapturemanager) = %{version}
Requires:       crate(%{pkgname}/mtlcapturescope) = %{version}
Requires:       crate(%{pkgname}/mtlcommandbuffer) = %{version}
Requires:       crate(%{pkgname}/mtlcommandencoder) = %{version}
Requires:       crate(%{pkgname}/mtlcommandqueue) = %{version}
Requires:       crate(%{pkgname}/mtlcomputecommandencoder) = %{version}
Requires:       crate(%{pkgname}/mtlcomputepass) = %{version}
Requires:       crate(%{pkgname}/mtlcomputepipeline) = %{version}
Requires:       crate(%{pkgname}/mtlcounters) = %{version}
Requires:       crate(%{pkgname}/mtldefines) = %{version}
Requires:       crate(%{pkgname}/mtldepthstencil) = %{version}
Requires:       crate(%{pkgname}/mtldevice) = %{version}
Requires:       crate(%{pkgname}/mtldrawable) = %{version}
Requires:       crate(%{pkgname}/mtldynamiclibrary) = %{version}
Requires:       crate(%{pkgname}/mtlevent) = %{version}
Requires:       crate(%{pkgname}/mtlfence) = %{version}
Requires:       crate(%{pkgname}/mtlfunctionconstantvalues) = %{version}
Requires:       crate(%{pkgname}/mtlfunctiondescriptor) = %{version}
Requires:       crate(%{pkgname}/mtlfunctionhandle) = %{version}
Requires:       crate(%{pkgname}/mtlfunctionlog) = %{version}
Requires:       crate(%{pkgname}/mtlfunctionstitching) = %{version}
Requires:       crate(%{pkgname}/mtlheap) = %{version}
Requires:       crate(%{pkgname}/mtlindirectcommandbuffer) = %{version}
Requires:       crate(%{pkgname}/mtlindirectcommandencoder) = %{version}
Requires:       crate(%{pkgname}/mtlintersectionfunctiontable) = %{version}
Requires:       crate(%{pkgname}/mtliocommandbuffer) = %{version}
Requires:       crate(%{pkgname}/mtliocommandqueue) = %{version}
Requires:       crate(%{pkgname}/mtliocompressor) = %{version}
Requires:       crate(%{pkgname}/mtllibrary) = %{version}
Requires:       crate(%{pkgname}/mtllinkedfunctions) = %{version}
Requires:       crate(%{pkgname}/mtlparallelrendercommandencoder) = %{version}
Requires:       crate(%{pkgname}/mtlpipeline) = %{version}
Requires:       crate(%{pkgname}/mtlpixelformat) = %{version}
Requires:       crate(%{pkgname}/mtlrasterizationrate) = %{version}
Requires:       crate(%{pkgname}/mtlrendercommandencoder) = %{version}
Requires:       crate(%{pkgname}/mtlrenderpass) = %{version}
Requires:       crate(%{pkgname}/mtlrenderpipeline) = %{version}
Requires:       crate(%{pkgname}/mtlresource) = %{version}
Requires:       crate(%{pkgname}/mtlresourcestatecommandencoder) = %{version}
Requires:       crate(%{pkgname}/mtlresourcestatepass) = %{version}
Requires:       crate(%{pkgname}/mtlsampler) = %{version}
Requires:       crate(%{pkgname}/mtlstageinputoutputdescriptor) = %{version}
Requires:       crate(%{pkgname}/mtltexture) = %{version}
Requires:       crate(%{pkgname}/mtltypes) = %{version}
Requires:       crate(%{pkgname}/mtlvertexdescriptor) = %{version}
Requires:       crate(%{pkgname}/mtlvisiblefunctiontable) = %{version}
Provides:       crate(%{pkgname}/all) = %{version}

%description -n %{name}+all
This metapackage enables feature "all" for the Rust objc2-metal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+alloc
Summary:        Bindings to the Metal framework - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block2-0.5/alloc) >= 0.5.1
Requires:       crate(objc2-0.5/alloc) >= 0.5.2
Requires:       crate(objc2-foundation-0.2/alloc) >= 0.2.2
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust objc2-metal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bitflags
Summary:        Bindings to the Metal framework - feature "bitflags"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bitflags-2) >= 2.5.0
Requires:       crate(objc2-foundation-0.2/bitflags) >= 0.2.2
Provides:       crate(%{pkgname}/bitflags) = %{version}

%description -n %{name}+bitflags
This metapackage enables feature "bitflags" for the Rust objc2-metal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+block2
Summary:        Bindings to the Metal framework - feature "block2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block2-0.5) >= 0.5.1
Requires:       crate(objc2-foundation-0.2/block2) >= 0.2.2
Provides:       crate(%{pkgname}/block2) = %{version}

%description -n %{name}+block2
This metapackage enables feature "block2" for the Rust objc2-metal crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Bindings to the Metal framework - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(bitflags-2/std) >= 2.5.0
Requires:       crate(block2-0.5/std) >= 0.5.1
Requires:       crate(objc2-0.5/std) >= 0.5.2
Requires:       crate(objc2-foundation-0.2/std) >= 0.2.2
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust objc2-metal crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+unstable-private
Summary:        Bindings to the Metal framework - feature "unstable-private"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/unstable-private) = %{version}

%description -n %{name}+unstable-private
This metapackage enables feature "unstable-private" for the Rust objc2-metal crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
