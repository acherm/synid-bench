function [bloom_number, bloom, base, left_peak,right_peak, bloom_ownership, ...
    odd_level, even_level, candidates, bridges] = ...
    CREATE_BLOOM(create_bloom_struct)

graph = create_bloom_struct.graph;
search_level = create_bloom_struct.search_level;
bloom_number = create_bloom_struct.bloom_number;
bloom = create_bloom_struct.bloom;
bloom_ownership = create_bloom_struct.bloom_ownership;
left_peak = create_bloom_struct.left_peak;
right_peak = create_bloom_struct.right_peak;
base = create_bloom_struct.base;
bottleneck = create_bloom_struct.bottleneck;
init_right = create_bloom_struct.init_right;
init_left = create_bloom_struct.init_left;
ownership = create_bloom_struct.ownership;
even_level = create_bloom_struct.even_level;
odd_level = create_bloom_struct.odd_level;
candidates = create_bloom_struct.candidates;
anomalies = create_bloom_struct.anomalies;
bridges = create_bloom_struct.bridges;
% define bloom: give a number, assign it left_peak,
% right_peak, and base.
level = min(even_level,odd_level);
bloom_number = bloom_number + 1; % add new bloom.
bloom_vertices = find(ownership); % all things in trees are bloom.



base(bloom_number) = bottleneck;
left_peak(bloom_number) = init_left;
right_peak(bloom_number) = init_right;

index = @ (search_level) search_level+1;
1;
for y = bloom_vertices % assign other levels and find extra bridges
    bloom(y) = bloom_number;
    bloom_ownership(y) = ownership(y);
    if mod(level(y),2)==0 % y is outer
        odd_level(y) = 2*search_level + 1 - ...
            even_level(y);
    else % y inner
        even_level(y) = 2 * search_level + 1 - ...
            odd_level(y);
        candidates{index(even_level(y))} = ...
            [candidates{index(even_level(y))}, y];
        for z = anomalies{y}
            j = (even_level(y) + even_level(z)) / 2;
            bridges{index(j)} = [bridges{index(j)}, graph.get_e_from_vs(y,z)];
            % I don't understand why the algorithm requires us to mark y,z
            % used for future DDFS. I am ignoring for now, hoping it is not
            % necessary! TODO.
        end
    end
end

end

