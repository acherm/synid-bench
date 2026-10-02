classdef Tone < Signal
    properties (GetAccess = public, SetAccess = private)
        amplitude_dB_SPL@double
        frequency@double
        nSamples
        duration
    end
    methods
        function obj = Tone(duration, amplitude_dB_SPL, frequency)
            obj.duration = duration;
            obj.amplitude_dB_SPL = amplitude_dB_SPL;
            obj.frequency = frequency;            
            obj.nSamples = getappdata(0, 'samplingFrequency') * obj.duration;
        end
        function data = getData(obj)
            dataWithoutWindow = obj.amplitude .* sin(2*pi*obj.frequency .* (1:obj.nSamples)/getappdata(0, 'samplingFrequency'))';
            data = dataWithoutWindow .* window(@tukeywin, obj.nSamples);
        end
        str = struct(obj)
    end
    methods (Static = true)
        obj = importStruct(struct)
    end
end